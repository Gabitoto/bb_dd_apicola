#!/usr/bin/env python3
"""
Script para conectar y cargar datos en la base de datos apícola PostgreSQL
Autor: Sistema de Gestión Apícola
Fecha: 2024
"""

import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
from datetime import datetime, date
import logging
import os
from typing import Dict, List, Optional, Tuple

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('apicola_db.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ApiculturaBD:
    """Clase para manejar la conexión y operaciones de la base de datos apícola"""
    
    def __init__(self, host: str = 'localhost', port: int = 5432, 
                 database: str = 'apicultura', user: str = 'postgres', 
                 password: str = 'password'):
        """
        Inicializar conexión a la base de datos
        
        Args:
            host: Dirección del servidor PostgreSQL
            port: Puerto de conexión
            database: Nombre de la base de datos
            user: Usuario de PostgreSQL
            password: Contraseña del usuario
        """
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
        """
        Establecer conexión con la base de datos
        
        Returns:
            bool: True si la conexión fue exitosa, False en caso contrario
        """
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
        """
        Ejecutar una consulta SELECT
        
        Args:
            query: Consulta SQL
            params: Parámetros para la consulta
            
        Returns:
            List[Dict]: Resultados de la consulta
        """
        try:
            self.cursor.execute(query, params)
            resultados = self.cursor.fetchall()
            logger.info(f"Consulta ejecutada: {len(resultados)} registros obtenidos")
            return resultados
        except psycopg2.Error as e:
            logger.error(f"Error al ejecutar consulta: {e}")
            return []
    
    def ejecutar_transaccion(self, queries: List[Tuple[str, tuple]]) -> bool:
        """
        Ejecutar múltiples consultas en una transacción
        
        Args:
            queries: Lista de tuplas (query, params)
            
        Returns:
            bool: True si todas las consultas fueron exitosas
        """
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
    
    # MÉTODOS PARA INSERTAR DATOS
    
    def insertar_apicultor(self, nombre: str, apellido: str) -> Optional[int]:
        """Insertar un nuevo apicultor"""
        query = """
        INSERT INTO apicultor (nombre, apellido) 
        VALUES (%s, %s) 
        RETURNING id_apicultor
        """
        try:
            self.cursor.execute(query, (nombre, apellido))
            id_apicultor = self.cursor.fetchone()['id_apicultor']
            self.connection.commit()
            logger.info(f"Apicultor insertado: {nombre} {apellido} (ID: {id_apicultor})")
            return id_apicultor
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error al insertar apicultor: {e}")
            return None
    
    def insertar_analista(self, nombres: str, apellidos: str, contacto: str = None) -> Optional[int]:
        """Insertar un nuevo analista"""
        query = """
        INSERT INTO analista (nombres, apellidos, contacto) 
        VALUES (%s, %s, %s) 
        RETURNING id_analista
        """
        try:
            self.cursor.execute(query, (nombres, apellidos, contacto))
            id_analista = self.cursor.fetchone()['id_analista']
            self.connection.commit()
            logger.info(f"Analista insertado: {nombres} {apellidos} (ID: {id_analista})")
            return id_analista
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error al insertar analista: {e}")
            return None
    
    def insertar_apiario(self, id_apicultor: int, nombre_apiario: str, 
                        cant_colmenas: int, localidad: str, 
                        latitud: float = None, longitud: float = None) -> Optional[int]:
        """Insertar un nuevo apiario"""
        query = """
        INSERT INTO apiarios (id_apicultor, nombre_apiario, cant_colmenas, 
                             localidad, latitud, longitud) 
        VALUES (%s, %s, %s, %s, %s, %s) 
        RETURNING id_apiario
        """
        try:
            self.cursor.execute(query, (id_apicultor, nombre_apiario, cant_colmenas, 
                                      localidad, latitud, longitud))
            id_apiario = self.cursor.fetchone()['id_apiario']
            self.connection.commit()
            logger.info(f"Apiario insertado: {nombre_apiario} (ID: {id_apiario})")
            return id_apiario
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error al insertar apiario: {e}")
            return None
    
    def insertar_especie(self, nombre_cientifico: str, nombre_comun: str, 
                        familia: str) -> Optional[int]:
        """Insertar una nueva especie"""
        query = """
        INSERT INTO especies (nombre_cientifico, nombre_comun, familia) 
        VALUES (%s, %s, %s) 
        RETURNING id_especie
        """
        try:
            self.cursor.execute(query, (nombre_cientifico, nombre_comun, familia))
            id_especie = self.cursor.fetchone()['id_especie']
            self.connection.commit()
            logger.info(f"Especie insertada: {nombre_comun} (ID: {id_especie})")
            return id_especie
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error al insertar especie: {e}")
            return None
    
    def insertar_tambor(self, num_registro: str) -> Optional[int]:
        """Insertar un nuevo tambor"""
        query = """
        INSERT INTO tambor (num_registro) 
        VALUES (%s) 
        RETURNING id_tambor
        """
        try:
            self.cursor.execute(query, (num_registro,))
            id_tambor = self.cursor.fetchone()['id_tambor']
            self.connection.commit()
            logger.info(f"Tambor insertado: {num_registro} (ID: {id_tambor})")
            return id_tambor
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error al insertar tambor: {e}")
            return None
    
    def insertar_muestra(self, id_analista: int, fecha_extraccion: date, 
                        fecha_analisis: date = None, num_registro: str = None, 
                        observaciones: str = None) -> Optional[int]:
        """Insertar una nueva muestra"""
        query = """
        INSERT INTO muestra (id_analista, fecha_extraccion, fecha_analisis, 
                           num_registro, observaciones) 
        VALUES (%s, %s, %s, %s, %s) 
        RETURNING id_muestra
        """
        try:
            self.cursor.execute(query, (id_analista, fecha_extraccion, fecha_analisis, 
                                      num_registro, observaciones))
            id_muestra = self.cursor.fetchone()['id_muestra']
            self.connection.commit()
            logger.info(f"Muestra insertada: {num_registro} (ID: {id_muestra})")
            return id_muestra
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error al insertar muestra: {e}")
            return None
    
    def insertar_analisis_palinologico(self, id_muestra: int, id_especie: int, 
                                     cantidad_granos: int, marca_especial: str = None, 
                                     porcentaje: float = None) -> bool:
        """Insertar un análisis palinológico"""
        query = """
        INSERT INTO analisis_palinologico (id_muestra, id_especie, cantidad_granos, 
                                         marca_especial, porcentaje) 
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, (id_muestra, id_especie, cantidad_granos, 
                                      marca_especial, porcentaje))
            self.connection.commit()
            logger.info(f"Análisis palinológico insertado para muestra {id_muestra}")
            return True
        except psycopg2.Error as e:
            self.connection.rollback()
            logger.error(f"Error al insertar análisis palinológico: {e}")
            return False
    
    # MÉTODOS DE CONSULTA
    
    def obtener_apicultores(self) -> List[Dict]:
        """Obtener todos los apicultores"""
        query = "SELECT * FROM apicultor ORDER BY apellido, nombre"
        return self.ejecutar_consulta(query)
    
    def obtener_especies(self) -> List[Dict]:
        """Obtener todas las especies"""
        query = "SELECT * FROM especies ORDER BY nombre_comun"
        return self.ejecutar_consulta(query)
    
    def obtener_muestras_pendientes(self) -> List[Dict]:
        """Obtener muestras pendientes de análisis"""
        query = """
        SELECT m.*, an.nombres || ' ' || an.apellidos as analista
        FROM muestra m
        JOIN analista an ON m.id_analista = an.id_analista
        WHERE m.fecha_analisis IS NULL
        ORDER BY m.fecha_extraccion
        """
        return self.ejecutar_consulta(query)
    
    def obtener_resumen_apiarios(self) -> List[Dict]:
        """Obtener resumen de apiarios por apicultor"""
        query = """
        SELECT 
            ap.nombre || ' ' || ap.apellido as apicultor,
            COUNT(a.id_apiario) as total_apiarios,
            SUM(a.cant_colmenas) as total_colmenas
        FROM apicultor ap
        LEFT JOIN apiarios a ON ap.id_apicultor = a.id_apicultor
        GROUP BY ap.id_apicultor, ap.nombre, ap.apellido
        ORDER BY total_colmenas DESC NULLS LAST
        """
        return self.ejecutar_consulta(query)
    
    # MÉTODOS PARA CARGAR DATOS DESDE ARCHIVOS
    
    def cargar_desde_csv(self, archivo_csv: str, tabla: str) -> bool:
        """
        Cargar datos desde un archivo CSV
        
        Args:
            archivo_csv: Ruta del archivo CSV
            tabla: Nombre de la tabla destino
            
        Returns:
            bool: True si la carga fue exitosa
        """
        try:
            df = pd.read_csv(archivo_csv)
            logger.info(f"Cargando {len(df)} registros desde {archivo_csv} a tabla {tabla}")
            
            # Aquí puedes personalizar la carga según la tabla
            if tabla == 'apicultor':
                for _, row in df.iterrows():
                    self.insertar_apicultor(row['nombre'], row['apellido'])
            elif tabla == 'especies':
                for _, row in df.iterrows():
                    self.insertar_especie(row['nombre_cientifico'], 
                                        row['nombre_comun'], row['familia'])
            # Agregar más tablas según necesites
            
            return True
        except Exception as e:
            logger.error(f"Error al cargar CSV: {e}")
            return False


def main():
    """Función principal para probar la conexión y operaciones básicas"""
    
    # Configuración de la base de datos
    # MODIFICA ESTOS VALORES SEGÚN TU CONFIGURACIÓN
    DB_CONFIG = {
        'host': 'localhost',
        'port': 5432,
        'database': 'apicultura',
        'user': 'postgres',
        'password': 'tu_password_aqui'
    }
    
    # Crear instancia de la clase
    db = ApiculturaBD(**DB_CONFIG)
    
    try:
        # Conectar a la base de datos
        if not db.conectar():
            logger.error("No se pudo conectar a la base de datos")
            return
        
        # Probar algunas operaciones
        logger.info("=== PROBANDO OPERACIONES BÁSICAS ===")
        
        # 1. Obtener resumen de apiarios
        logger.info("1. Resumen de apiarios:")
        resumen = db.obtener_resumen_apiarios()
        for fila in resumen:
            print(f"  - {fila['apicultor']}: {fila['total_apiarios']} apiarios, {fila['total_colmenas']} colmenas")
        
        # 2. Obtener muestras pendientes
        logger.info("2. Muestras pendientes de análisis:")
        pendientes = db.obtener_muestras_pendientes()
        for muestra in pendientes:
            print(f"  - {muestra['num_registro']}: {muestra['analista']} - {muestra['fecha_extraccion']}")
        
        # 3. Insertar un nuevo apicultor (ejemplo)
        logger.info("3. Insertando nuevo apicultor:")
        nuevo_id = db.insertar_apicultor("Ejemplo", "Prueba")
        if nuevo_id:
            print(f"  - Apicultor insertado con ID: {nuevo_id}")
        
        # 4. Obtener todas las especies
        logger.info("4. Especies disponibles:")
        especies = db.obtener_especies()
        for especie in especies[:5]:  # Solo mostrar las primeras 5
            print(f"  - {especie['nombre_comun']} ({especie['nombre_cientifico']})")
        
        logger.info("=== OPERACIONES COMPLETADAS ===")
        
    except Exception as e:
        logger.error(f"Error en la ejecución principal: {e}")
    
    finally:
        # Cerrar conexión
        db.desconectar()


if __name__ == "__main__":
    main()
