# Vehicle Data Explorer - Interactive Vehicle Analysis

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://proyecto-sprint-7-dk8h.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Vehicle Data Explorer** is an interactive web application that transforms complex vehicle data into intuitive and actionable visualizations. Designed to democratize data analysis, it enables users of all skill levels to explore patterns, trends, and relationships in a used vehicle dataset through a simple yet powerful interface.

The project emerged from the need to create more than just a static analysis: a living tool that demonstrates comprehensive software engineering skills, from initial analysis to production deployment. Using modern technologies like Streamlit and Plotly, the application offers interactive charts with filtering, zoom, and on-demand detail capabilities, making exploratory data analysis accessible to everyone.

## 🎯 Core Skills
* Rapid Exploratory Analysis: Data cleaning, exploratory data analysis (EDA), pattern identification. Enables identification of distributions, correlations, and outliers in vehicle data.
* Interactive Visualizations: Generates dynamic histograms and scatter plots using Plotly Express.
* Intuitive Interface: Built with Streamlit for a seamless, user-friendly experience.
* Deployment: Deployed on multiple cloud platforms (Streamlit Cloud)

## 🛠️ Tech Stack 
* **Frontend** -> Streamlit, Plotly Express
* **Backend** -> Python 3.8+, Pandas, NumPy
* **Deployment** -> Streamlit Cloud
* **Deployment** -> Virtual environments, Git, Jupyter Notebooks

## 🚀 Demo
Test the application now!

🔗 *Streamlit Cloud*
👉 https://vehicle-data-explorer.streamlit.app/


## Documentation Guide
We recommend reviewing the files in the following order:

1. [README.md](README.md): Complete project documentation (this file).
2. [vehicles_us.csv](vehicles_us.csv): Primary dataset used in the analysis.
3. [requirements.txt](requirements.txt): Required Python dependencies.
5. [notebooks/EDA.ipynb](notebooks/EDA.ipynb): Exploratory Data Analysis notebook (EDA).
6. [app.py](app.py): Main Streamlit application file.

## Local Setup
o run this project locally, follow these steps:
1. Clone the repository:

   git clone https://github.com/RosellaAM/Vehicle-Data-Explorer.git
   cd vehicle-data-explore

3. Set up virtual environment:

   python -m venv venv
    source venv/bin/activate  # Linux/Mac

5. Install required packages:

   pip install -r requirements.txt

7. Launch the application:

   streamlit run app.py
