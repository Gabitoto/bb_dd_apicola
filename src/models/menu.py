"""
Módulo para manejar las funcionalidades del menú principal
"""

from src.models.consultas import ejecutar_consulta_personalizada
from src.models.dashboards import mostrar_dashboards
from src.models.gestion_datos import agregar_nuevos_datos

def mostrar_menu():
    """Muestra el menú principal de la aplicación"""
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Realizar consulta personalizada")
    print("2. Ver Dashboards")
    print("3. Agregar nuevos datos")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

def procesar_opcion(opcion, db):
    """Procesa la opción seleccionada por el usuario"""
    if opcion == "1":
        ejecutar_consulta_personalizada(db)
    elif opcion == "2":
        mostrar_dashboards(db)
    elif opcion == "3":
        agregar_nuevos_datos(db)
    elif opcion == "4":
        print("¡Hasta pronto!")
        return False
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
    return True 