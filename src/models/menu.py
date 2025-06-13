"""
Módulo para manejar las funcionalidades del menú principal
"""

from src.models.dashboards import mostrar_dashboards
from src.models.gestion_datos import agregar_nuevos_datos

def mostrar_menu():
    """Muestra el menú principal de la aplicación"""
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ver Dashboards")
    print("2. Agregar nuevos datos")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

def procesar_opcion(opcion, db):
    """Procesa la opción seleccionada por el usuario"""
    if opcion == "1":
        mostrar_dashboards(db)
    elif opcion == "2":
        agregar_nuevos_datos(db)
    elif opcion == "3":
        print("¡Hasta pronto!")
        return False
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
    return True 