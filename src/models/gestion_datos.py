"""
Módulo para manejar la gestión de datos en la base de datos
"""

from src.models.apicultor import Apicultor
from src.utils.logger import logger

def agregar_nuevos_datos(db):
    """Permite agregar nuevos datos a la base de datos"""
    print("\n=== AGREGAR NUEVOS DATOS ===")
    print("1. Agregar nuevo apicultor")
    print("2. Agregar nueva colmena")
    print("3. Agregar nueva muestra")
    print("4. Volver al menú principal")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        nombre = input("Nombre del apicultor: ")
        apellido = input("Apellido del apicultor: ")
        apicultor_model = Apicultor(db)
        nuevo_id = apicultor_model.insertar(nombre, apellido)
        if nuevo_id:
            print(f"Apicultor agregado exitosamente con ID: {nuevo_id}")
    
    # Aquí se pueden agregar más opciones para insertar otros tipos de datos 