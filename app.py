import pandas as pd
import plotly.express as px
import streamlit as st

# Carga el dataset de vehículos.
vehicles = pd.read_csv("/Users/Rosella/Downloads/vehicles_us.csv")

# Crea el titulo de la aplicación.
st.title('Análisis  de Vehículos Usados')

# Muestra una muestra de la base de datos en la aplicación.
st.subheader('Vista previa de los datos (10 registros aleatorios)')
st.dataframe(vehicles.sample(10))
with st.expander('Ver datos completos'):
    # Muestra dataset completo (limitado a 500 filas).
    st.dataframe(vehicles.head(500))

# Muestra casillas de verificación para seleccionar la grafica a mostrar.
show_hist_price = st.checkbox('Mostrar Histograma de Precios', value=True)
show_scatter_km_price = st.checkbox('Mostrar Gráfica de Dispersión de Kilometraje vs Precio', value=True)

# Crea histograma de precios y la acción que se realizara al picarle al checkbox.
if show_hist_price:
    # Carga el mensaje.
    st.write('Histograma del Promedio de Precios de Vehículos Usados')
    # Carga slide bar con el rango de precios.
    price_range = st.slider('Rango de Precios(USD)', 
                            min_value= int(vehicles['price'].min()), 
                            max_value= int(vehicles['price'].quantile(0.95)),
                            value=(5000, 50000))
    # Filtra los datos por el rango de precios seleccionados.
    vehicles_price_filt = vehicles[(vehicles['price'] >= price_range[0]) & (vehicles['price'] <= price_range[1])]
    # Crea el histograma.
    fig1= px.histogram(vehicles_price_filt,
                        x='price', 
                        nbins=50, 
                        title='Distribución de Precios de Vehículos', 
                        labels={'price' : 'Precio (USD)'}, 
                        color_discrete_sequence=['purple'])
    # Muestra el grafico interactivo en la aplicación.
    st.plotly_chart(fig1, use_container_width=True)

# Crea grafica de dispersión y la acción que se realizara al picarle al checkbox.
if show_scatter_km_price:
    # Carga el mensaje.
    st.write('Gráfica de Dispersión: Kilometraje vs Precio')
    # Carga side bar con filtros.
    st.sidebar.header('Filtros')
    selected_condition = st.sidebar.multiselect(
        'Condición del Vehículo',
        options=vehicles['condition'].unique(),
        default=['good', 'excellent'])
    # Filtra los datos por las condiciones seleccionadas.
    filtered_vehicles_by_con = vehicles[vehicles['condition'].isin(selected_condition)]
    # Crea grafica de dispersión verificando que si se apliquen los filtros.
    if len(filtered_vehicles_by_con) == 0:
        st.warning('No hay datos disponibles con los filtros seleccionados.')
    else:
        fig2 = px.scatter(filtered_vehicles_by_con, 
                           x='odometer',
                           y='price',
                           color='condition',
                           title='Relación Precio vs. Kilometraje',
                           labels={'odometer': 'Kilometraje', 'price': 'Precio (USD)'},
                           trendline='lowess')
    # Muestra el grafico interactivo en la aplicación.
    st.plotly_chart(fig2, use_container_width=True)
