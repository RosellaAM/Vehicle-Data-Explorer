import pandas as pd
import plotly.express as px
import streamlit as st

# Carga el dataset de vehículos.
vehicles = pd.read_csv("vehicles_us.csv")

# Crea el titulo de la aplicación.
st.title('Análisis de Vehículos Usados')

# Muestra una muestra de la base de datos en la aplicación.
st.subheader('Vista previa de los datos')
st.dataframe(vehicles.sample(10))
full_data = st.button('Ver datos completos')
if full_data:
    with st.expander('Ver'):
        # Muestra dataset completo (limitado a 500 filas).
        st.dataframe(vehicles.head(500))

# Muestra casillas de verificación para seleccionar la grafica a mostrar.
show_hist_price = st.checkbox('Mostrar Histograma de Precios', value=False)
show_scatter_km_price = st.checkbox('Mostrar Gráfica de Dispersión de Kilometraje vs Precio', value=False)
show_bar_fuel = st.checkbox('Morstrar Gráfica de Barras de Precio por Combustible', value=False)
show_boxplot_days = st.checkbox('Mostrar Gráfica de Distribución de Días en el Mercado por Condición del Vehículo', value=False)
show_corr = st.checkbox('Mostrar la Matriz de Correlación entre las Diferentes Variables', value=False)

# Crea divisor para separar el dataframe de las graficas.
st.divider()

# Crea histograma de precios y la acción que se realizara al picarle al checkbox.
if show_hist_price:
    # Carga el mensaje.
    st.write('***Histograma del promedio de precios de vehículos usados***')
    # Carga slide bar con el rango de precios.
    price_range = st.slider('Rango de Precios(USD)', 
                            min_value= int(vehicles['price'].min()), 
                            max_value= int(vehicles['price'].max()),
                            value=(5000, 50000))
    # Filtra los datos por el rango de precios seleccionados.
    vehicles_price_filt = vehicles[(vehicles['price'] >= price_range[0]) & (vehicles['price'] <= price_range[1])]
    # Crea el histograma.
    fig1= px.histogram(vehicles_price_filt,
                        x='price', 
                        nbins=50, 
                        title='Distribución de Precios de Vehículos', 
                        labels={'price' : 'Precio (USD)'}, 
                        color_discrete_sequence=['purple']
                        )
    # Muestra el gráfico interactivo en la aplicación.
    st.plotly_chart(fig1, use_container_width=True)
    # Crea divisor entre las gráficas.
    st.divider()


# Crea grafica de dispersión y la acción que se realizara al picarle al checkbox.
if show_scatter_km_price:
    # Carga el mensaje.
    st.write('***Gráfica de dispersión: kilometraje vs precio***')
    st.caption('Selecciona los diferentes filtros para ver mas información sobre como afectan las condiciones el kilometraje y precio.')
    # Carga pills con filtros.
    selected_condition_km = st.pills("Filtros", 
             selection_mode="multi", 
             options=vehicles['condition'].unique(), 
             default=['good', 'excellent']
             )
    # Filtra los datos por las condiciones seleccionadas.
    filtered_vehicles_by_con = vehicles[vehicles['condition'].isin(selected_condition_km)]
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
                           trendline='lowess'
                           )
    # Muestra el gráfico interactivo en la aplicación.
    st.plotly_chart(fig2, use_container_width=True)
    # Crea divisor entre las gráficas.
    st.divider()


# Crea gráfica de barras y la acción que se realizara al picarle al checkbox.
if show_bar_fuel:
    # Carga el mensaje.
    st.write('***Gráfica de barras del precio por tipo de combustible***')
    st.caption('Selecciona la varibale que quieres comparar.')
    # Filtra los datos para obtener la media, mediana y conteo.
    metric = st.selectbox("Elije una variable", 
                          options=['Promedio', 'Mediana', 'Conteo de Vehículos']
                          )
    if metric == 'Promedio':
        data = mean_days = vehicles.groupby('fuel')['price'].mean().reset_index()
    elif metric == 'Mediana':
        data = median_days = vehicles.groupby('fuel')['price'].median().reset_index()
    else:
        data = count_days = vehicles['fuel'].value_counts().reset_index()
        data.columns = ['fuel', 'counts']
    # Crea gráfica de barras.
    fig3 = px.bar(data, 
                  x='fuel', 
                  y='price',
                  title=f'Precio {metric} por Tipo de Combustible',
                  labels={'fuel': 'Tipo de Combustible', 'price': 'Precio (USD)'},
                  color='fuel',
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    # Muestra el gráfico interactivo en la aplicación.
    st.plotly_chart(fig3, use_container_width=True)
    # Crea divisor entre las gráficas.
    st.divider()


# Crea gráfica boxplot.
if show_boxplot_days:
    # Carga el mensaje.
    st.write('***Gráfica de distribución de los días en el mercado por su condición***')
    st.caption('Modifíca los filtros para ver las diferentes condiciones')
    # Carga pills con filtros.
    selected_condition_d = st.pills("Filtros", 
             selection_mode="multi", 
             options=vehicles['condition'].unique(), 
             default=['good', 'excellent']
             )
    # Filtra los datos.
    filtered_data_by_con_d = vehicles[vehicles['condition'].isin(selected_condition_d)]
    # Verifica que si hay datos con las condicones aplicadas.
    if len(filtered_data_by_con_d) == 0:
        st.warning('No hay datos disponibles con los filtros seleccionados.')
    else:
        fig4 = px.box(filtered_data_by_con_d,
                      x='condition',
                      y='days_listed',
                      title='Distribución de Días en el Mercado por Condión',
                      labels={'condition': 'Condición del Vehículo', 'days_listed': 'Días en el Mercado'},
                      color='condition'
                      )
    # Muestra el gráfico interactiva en la aplicación.
    st.plotly_chart(fig4, use_container_width=True)
    # Crea divisor entre las graficas.
    st.divider()

