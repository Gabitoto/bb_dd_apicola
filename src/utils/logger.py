"""
Configuración del sistema de logging
"""

import logging

def setup_logger():
    """Configura y retorna el logger principal de la aplicación"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('apicola_db.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logger() 