"""
Módulo para manejar la gestión de datos en la base de datos
"""

from src.models.apicultor import Apicultor, Apiario
from src.utils.logger import logger

def eliminar_apicultor(db):
    """Permite eliminar un apicultor de la base de datos"""
    print("\n=== ELIMINAR APICULTOR ===")
    id_apicultor = input("Ingrese el ID del apicultor a eliminar: ")
    
    try:
        apicultor_model = Apicultor(db)
        if apicultor_model.eliminar(id_apicultor):
            print("Apicultor eliminado exitosamente")
        else:
            print("No se pudo eliminar el apicultor. Verifique que el ID exista.")
    except Exception as e:
        logger.error(f"Error al eliminar apicultor: {str(e)}")
        print("Ocurrió un error al intentar eliminar el apicultor")

def agregar_nuevos_datos(db):
    """Permite agregar nuevos datos a la base de datos"""
    print("\n=== AGREGAR NUEVOS DATOS ===")
    print("1. Agregar nuevo apicultor")
    print("2. Agregar nuevo apiario")
    print("3. Eliminar apicultor")
    print("4. Volver al menú principal")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        nombre = input("Nombre del apicultor: ")
        apellido = input("Apellido del apicultor: ")
        apicultor_model = Apicultor(db)
        nuevo_id = apicultor_model.insertar(nombre, apellido)
        if nuevo_id:
            print(f"Apicultor agregado exitosamente con ID: {nuevo_id}")
    elif opcion == "2":
        nombre = input("Nombre del apiario: ")
        id_apicultor = input("ID del apicultor: ")
        apiario_model = Apiario(db)
        nuevo_id = apiario_model.insertar(nombre, id_apicultor)
        if nuevo_id:
            print(f"Apiario agregado exitosamente con ID: {nuevo_id}")
    elif opcion == "3":
        eliminar_apicultor(db)
    
    # Aquí se pueden agregar más opciones para insertar otros tipos de datos 