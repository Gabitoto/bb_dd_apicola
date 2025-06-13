"""
Modelo para manejar las operaciones relacionadas con apicultores
"""

from typing import Dict, List, Optional
from src.database.connection import DatabaseConnection
from src.utils.logger import logger

class Apicultor:
    def __init__(self, db: DatabaseConnection):
        self.db = db
    
    def insertar(self, nombre: str, apellido: str) -> Optional[int]:
        """Insertar un nuevo apicultor"""
        query = """
        INSERT INTO apicultor (nombre, apellido) 
        VALUES (%s, %s) 
        RETURNING id_apicultor
        """
        try:
            self.db.cursor.execute(query, (nombre, apellido))
            id_apicultor = self.db.cursor.fetchone()['id_apicultor']
            self.db.connection.commit()
            logger.info(f"Apicultor insertado: {nombre} {apellido} (ID: {id_apicultor})")
            return id_apicultor
        except Exception as e:
            self.db.connection.rollback()
            logger.error(f"Error al insertar apicultor: {e}")
            return None
    
    def obtener_todos(self) -> List[Dict]:
        """Obtener todos los apicultores"""
        query = "SELECT * FROM apicultor ORDER BY apellido, nombre"
        return self.db.ejecutar_consulta(query)
    
    def obtener_por_id(self, id_apicultor: int) -> Optional[Dict]:
        """Obtener un apicultor por su ID"""
        query = "SELECT * FROM apicultor WHERE id_apicultor = %s"
        resultados = self.db.ejecutar_consulta(query, (id_apicultor,))
        return resultados[0] if resultados else None 
    
    def eliminar(self, id_apicultor: int) -> bool:
        """Eliminar un apicultor por su ID"""
        # Primero verificamos si el apicultor existe
        if not self.obtener_por_id(id_apicultor):
            return False
            
        query = "DELETE FROM apicultor WHERE id_apicultor = %s"
        try:
            self.db.cursor.execute(query, (id_apicultor,))
            self.db.connection.commit()
            logger.info(f"Apicultor eliminado (ID: {id_apicultor})")
            return True
        except Exception as e:
            self.db.connection.rollback()
            logger.error(f"Error al eliminar apicultor: {e}")
            return False
    
    def cantidad_de_apiarios(self, id_apicultor: int) -> Optional[Dict]:
        "Funcion para ver la cantidad de apiarios que poseen cada apicultor"
        query = """
        SELECT 
            a.nombre || ' ' || a.apellido as nombre_completo,
            SUM(ap.cant_colmenas) as total_colmenas
        FROM apicultor a
        LEFT JOIN apiarios ap ON a.id_apicultor = ap.id_apicultor
        GROUP BY a.id_apicultor, a.nombre, a.apellido
        ORDER BY total_colmenas DESC
        """
        return self.db.ejecutar_consulta(query)

class Apiario:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def insertar(self, nombre: str, id_apicultor: int) -> Optional[int]:
        """Insertar un nuevo apiario"""
        query = """
        INSERT INTO apiario (nombre, id_apicultor)
        VALUES (%s, %s)
        RETURNING id_apiario
        """
        try:
            self.db.cursor.execute(query, (nombre, id_apicultor))
            id_apiario = self.db.cursor.fetchone()['id_apiario']
            self.db.connection.commit()
            logger.info(f"Apiario insertado: {nombre} (ID: {id_apiario})")
            return id_apiario
        except Exception as e:
            self.db.connection.rollback()
            logger.error(f"Error al insertar apiario: {e}")
            return None
        
    def obtener_todos(self) -> List[Dict]:
        """Obtener todos los apicultores"""
        query = "SELECT * FROM apicultor ORDER BY apellido, nombre"
        return self.db.ejecutar_consulta(query)
    
    def obtener_por_id(self, id_apicultor: int) -> Optional[Dict]:
        """Obtener un apicultor por su ID"""
        query = "SELECT * FROM apicultor WHERE id_apicultor = %s"