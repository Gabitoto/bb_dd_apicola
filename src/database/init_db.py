"""
Módulo para inicializar la base de datos
"""

from src.database.connection import DatabaseConnection
from src.utils.logger import logger
from config.config import DB_CONFIG

def inicializar_base_datos():
    """Verifica la conexión a la base de datos"""
    
    # Crear instancia de la conexión
    db = DatabaseConnection(**DB_CONFIG)
    
    try:
        # Conectar a la base de datos
        if not db.conectar():
            logger.error("No se pudo conectar a la base de datos")
            return False
        
        logger.info("Conexión a la base de datos establecida correctamente")
        return True
        
    except Exception as e:
        logger.error(f"Error al conectar a la base de datos: {e}")
        return False
    
    finally:
        # Cerrar conexión
        db.desconectar()

if __name__ == "__main__":
    inicializar_base_datos() 