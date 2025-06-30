# Sistema de Gestión Apícola

Sistema de gestión para apiarios que permite manejar apicultores, apiarios, muestras y análisis palinológicos presentado como Trabajo Practico Final de la catedra Bases de Datos.

## Estructura del Proyecto

```
bb_dd_apicola/
├── src/
│   ├── database/     # Manejo de conexión a la base de datos
│   ├── models/       # Modelos de datos
│   ├── utils/        # Utilidades
│   └── __init__.py
├── config/           # Configuración
├── main.py          # Punto de entrada
└── requirements.txt # Dependencias
```

## Requisitos

- Python 3.8+
- PostgreSQL 12+

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Configuración

1. Crear una base de datos PostgreSQL
2. Modificar `config/config.py` con los datos de conexión

## Uso

```bash
python main.py
```

## Características

- Gestión de apicultores
- Registro de apiarios
- Control de muestras
- Análisis palinológicos
- Reportes y estadísticas