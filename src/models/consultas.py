"""
Módulo para manejar las consultas personalizadas a la base de datos
"""

import pandas as pd
from src.utils.logger import logger

def ejecutar_consulta_personalizada(db):
    """Permite al usuario ejecutar una consulta SQL personalizada"""
    print("\n=== CONSULTA PERSONALIZADA ===")
    print("Ingrese su consulta SQL (o 'salir' para volver al menú):")
    while True:
        consulta = input("> ")
        if consulta.lower() == 'salir':
            break
        try:
            resultado = db.ejecutar_consulta(consulta)
            if resultado:
                df = pd.DataFrame(resultado)
                print("\nResultados:")
                print(df)
            else:
                print("La consulta no devolvió resultados")
        except Exception as e:
            logger.error(f"Error en la consulta: {e}") 
            
