# Vehicle Data Explorer - Análisis Interactivo de Vehículo

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://proyecto-sprint-7-dk8h.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Vehicle Data Explorer** es una aplicación web interactiva que transforma datos complejos de vehículos en visualizaciones intuitivas y accionables. Diseñada para democratizar el análisis de datos, permite a usuarios de todos los niveles explorar patrones, tendencias y relaciones en un dataset de vehículos usados mediante una interfaz simple pero poderosa.

El proyecto nació de la necesidad de crear más que un análisis estático: una herramienta viva que demostrara habilidades completas en ingeniería de software, desde el análisis inicial hasta el despliegue en producción. Utilizando tecnologías modernas como Streamlit y Plotly, la aplicación ofrece gráficos interactivos con capacidades de filtrado, zoom y detalles bajo demanda, haciendo que el análisis exploratorio de datos sea accesible para todos

## 🎯 Habilidades principales
* Análisis Exploratorio Rápido: Limpieza de datos, análisis exploratorio (EDA), identificación de patrones. Permite identificar distribuciones, correlaciones y valores atípicos en datos de vehículos.
* Visualizaciones Interactivas: Genera histogramas y gráficos de dispersión dinámicos utilizando Plotly Express.* 
* Interfaz Intuitiva: Diseñada con Streamlit para una experiencia de usuario fluida y sin complicaciones.*
* Deployment: Despliegue en múltiples plataformas cloud (Render, Streamlit Cloud)

## 🛠️ Stack Tecnológico
* **Frontend** -> Streamlit, Plotly Express
* **Backend** -> Python 3.8+, Pandas, NumPy
* **Despliegue** -> Render, Streamlit Cloud
* **Desarrollo** -> Entornos virtuales, Git, Jupyter Notebooks

## 🚀 Demo
¡Explora la aplicación ahora mismo!

🔗 *Enlace principal (Render.com)*

👉 https://proyecto-sprint-7-dk8h.onrender.com/


🔗 *Enlace alternativo más rápido (Streamlit Cloud)*

👉 https://proyecto-sprint-7-r-app.streamlit.app/


## Guia del Contenido 
Te recomiendo revisar los archivos en el siguiente orden:

1. [README.md](README.md): Este archivo con la documentación completa.
2. [vehicles_us.csv](vehicles_us.csv): Conjunto de datos utilizado en el proyecto.
3. [requirements.txt](requirements.txt): Lista de dependencias necesarias.
5. [notebooks/EDA.ipynb](notebooks/EDA.ipynb): Notebook de análisis exploratorio de datos (EDA).
6. [app.py](app.py): La aplicación principal desarrollada con Streamlit.

## Ejecución Local
Sigue estos pasos para ejecutar una copia local de este proyecto:
1. Clona el repositorio:
   git clone https://github.com/RosellaAM/Vehicle-Data-Explorer.git
   cd vehicle-data-explore

2. Crea el entorno vitual:
    python -m venv venv
    source venv/bin/activate  # Linux/Mac

3. Instala dependencias:
    pip install -r requirements.txt

4. Ejecuta la aplicación:
    streamlit run app.py
