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
    
    def cantidad_de_apiarios(self, id_apicultor: int) -> Optional[Dict]:
        "Funcion para ver la cantidad de apiarios que poseen cada apicultor"