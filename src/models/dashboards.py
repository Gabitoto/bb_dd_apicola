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
        SELECT 
            a.nombre || ' ' || a.apellido as nombre_completo,
            SUM(ap.cant_colmenas) as total_colmenas
        FROM apicultor a
        LEFT JOIN apiarios ap ON a.id_apicultor = ap.id_apicultor
        GROUP BY a.id_apicultor, a.nombre, a.apellido
        ORDER BY total_colmenas DESC
        """
        datos_colmenas = db.ejecutar_consulta(query_colmenas)
        df_colmenas = pd.DataFrame(datos_colmenas)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df_colmenas, x='nombre_completo', y='total_colmenas')
        plt.title('Cantidad de Colmenas por Apicultor')
        plt.xticks(rotation=45)
        plt.xlabel('Apicultor')
        plt.ylabel('Total de Colmenas')
        plt.tight_layout()
        plt.show()
        
        # Gráfico circular: Proporción de especies en las muestras
        query_especies = """
        SELECT 
            e.nombre_comun,
            SUM(ap.cantidad_granos) as cantidad
        FROM analisis_palinologico ap
        JOIN especies e ON ap.id_especie = e.id_especie
        GROUP BY e.nombre_comun
        ORDER BY cantidad DESC
        LIMIT 10
        """
        datos_especies = db.ejecutar_consulta(query_especies)
        df_especies = pd.DataFrame(datos_especies)
        
        plt.figure(figsize=(10, 6))
        plt.pie(df_especies['cantidad'], labels=df_especies['nombre_comun'], autopct='%1.1f%%')
        plt.title('Top 10 Especies más Frecuentes en las Muestras')
        plt.axis('equal')
        plt.show()
        
    except Exception as e:
        logger.error(f"Error al generar dashboards: {e}") 