"""
Script principal para la gestión de la base de datos apícola
"""

from src.database.connection import DatabaseConnection
from src.models.apicultor import Apicultor
from src.utils.logger import logger
from config.config import DB_CONFIG

def main():
    """Función principal para probar la conexión y operaciones básicas"""
    
    # Crear instancia de la conexión
    db = DatabaseConnection(**DB_CONFIG)
    
    try:
        # Conectar a la base de datos
        if not db.conectar():
            logger.error("No se pudo conectar a la base de datos")
            return
        
        # Crear instancia del modelo Apicultor
        apicultor_model = Apicultor(db)
        
        # Probar algunas operaciones
        logger.info("=== PROBANDO OPERACIONES BÁSICAS ===")
        
        # 1. Obtener todos los apicultores
        logger.info("1. Listando apicultores:")
        apicultores = apicultor_model.obtener_todos()
        for apicultor in apicultores:
            print(f"  - {apicultor['nombre']} {apicultor['apellido']}")
        
        # 2. Insertar un nuevo apicultor (ejemplo)
        logger.info("2. Insertando nuevo apicultor:")
        nuevo_id = apicultor_model.insertar("Ejemplo", "Prueba")
        if nuevo_id:
            print(f"  - Apicultor insertado con ID: {nuevo_id}")
        
        logger.info("=== OPERACIONES COMPLETADAS ===")
        
    except Exception as e:
        logger.error(f"Error en la ejecución principal: {e}")
    
    finally:
        # Cerrar conexión
        db.desconectar()

if __name__ == "__main__":
    main()