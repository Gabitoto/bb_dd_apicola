"""
Configuración de la base de datos y parámetros globales
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'database': os.getenv('DB_NAME', 'Gestión de apiarios'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', '123456lol')
} 