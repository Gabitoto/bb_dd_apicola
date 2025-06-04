"""
Módulo para manejar los dashboards y visualizaciones
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils.logger import logger

def mostrar_dashboards(db):
    """Muestra los dashboards con visualizaciones"""
    print("\n=== DASHBOARDS ===")
    
    # Gráfico de barras: Cantidad de colmenas por apicultor
    try:
        query_colmenas = """
        SELECT a.nombre, a.apellido, COUNT(c.id) as total_colmenas
        FROM apicultores a
        LEFT JOIN colmenas c ON a.id = c.apicultor_id
        GROUP BY a.id, a.nombre, a.apellido
        ORDER BY total_colmenas DESC
        """
        datos_colmenas = db.ejecutar_consulta(query_colmenas)
        df_colmenas = pd.DataFrame(datos_colmenas)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df_colmenas, x='nombre', y='total_colmenas')
        plt.title('Cantidad de Colmenas por Apicultor')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # Histograma: Proporción de especies en las muestras
        query_especies = """
        SELECT especie, COUNT(*) as cantidad
        FROM muestras
        GROUP BY especie
        """
        datos_especies = db.ejecutar_consulta(query_especies)
        df_especies = pd.DataFrame(datos_especies)
        
        plt.figure(figsize=(10, 6))
        plt.pie(df_especies['cantidad'], labels=df_especies['especie'], autopct='%1.1f%%')
        plt.title('Proporción de Especies en las Muestras')
        plt.axis('equal')
        plt.show()
        
    except Exception as e:
        logger.error(f"Error al generar dashboards: {e}") 