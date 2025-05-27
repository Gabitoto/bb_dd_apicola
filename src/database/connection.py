"""
Módulo para manejar la conexión a la base de datos
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Dict, List, Optional, Tuple
from src.utils.logger import logger

class DatabaseConnection:
    """Clase para manejar la conexión a la base de datos"""
    
    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self.connection_params = {
            'host': host,
            'port': port,
            'database': database,
            'user': user,
            'password': password
        }
        self.connection = None
        self.cursor = None
    
    def conectar(self) -> bool:
        """Establecer conexión con la base de datos"""
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
            logger.info("Conexión exitosa a la base de datos")
            return True
        except psycopg2.Error as e:
            logger.error(f"Error al conectar a la base de datos: {e}")
            return False
    
    def desconectar(self):
        """Cerrar conexión con la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        logger.info("Conexión cerrada")
    
    def ejecutar_consulta(self, query: str, params: tuple = None) -> List[Dict]:
        """Ejecutar una consulta SELECT"""
        try:
            self.cursor.execute(query, params)
            resultados = self.cursor.fetchall()
            logger.info(f"Consulta ejecutada: {len(resultados)} registros obtenidos")
            return resultados
        except psycopg2.Error as e:
            logger.error(f"Error al ejecutar consulta: {e}")
            return []
    
    def ejecutar_transaccion(self, queries: List[Tuple[str, tuple]]) -> bool:
        """Ejecutar múltiples consultas en una transacción"""
        try:
            for query, params in queries:
                self.cursor.execute(query, params)
            self.connection.commit()
            logger.info(f"Transacción completada: {len(queries)} consultas ejecutadas")
            return True
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error en transacción: {e}")
            return False 