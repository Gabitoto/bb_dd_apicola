"""
Script principal para la gestión de la base de datos apícola
"""

from src.database.connection import DatabaseConnection
from src.utils.logger import logger
from config.config import DB_CONFIG
from src.models.menu import mostrar_menu, procesar_opcion

def main():
    """Función principal de interfaz de la BBDD"""
    
    # Crear instancia de la conexión
    db = DatabaseConnection(**DB_CONFIG)
    
    try:
        # Conectar a la base de datos
        if not db.conectar():
            logger.error("No se pudo conectar a la base de datos")
            return
        
        while True:
            opcion = mostrar_menu()
            if not procesar_opcion(opcion, db):
                break
        
    except Exception as e:
        logger.error(f"Error en la ejecución principal: {e}")
    
    finally:
        # Cerrar conexión
        db.desconectar()

if __name__ == "__main__":
    main()