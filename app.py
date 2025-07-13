import pandas as pd
import plotly.express as px
import streamlit as st

# Carga el dataset de vehículos.
vehicles = pd.read_csv("vehicles_us.csv")

# Crea el título de la aplicación.
st.title('Análisis de Vehículos Usados')

# Muestra una muestra de la base de datos en la aplicación.
st.subheader('Vista previa de los datos')
st.dataframe(vehicles.sample(10))
full_data = st.button('Ver datos completos')
if full_data:
    with st.expander('Ver'):
        # Muestra dataset completo (limitado a 500 filas).
        st.dataframe(vehicles.head(500))

# Muestra casillas de verificación para seleccionar la gráfica a mostrar.
show_hist_price = st.checkbox('Mostrar Histograma de Precios', value=False)
show_scatter_km_price = st.checkbox('Mostrar Gráfica de Dispersión de Kilometraje vs Precio', value=False)
show_bar_fuel = st.checkbox('Morstrar Gráfica de Barras de Precio por Combustible', value=False)
show_boxplot_days = st.checkbox('Mostrar Gráfica de Distribución de Días en el Mercado por Condición del Vehículo', value=False)
show_corr = st.checkbox('Mostrar la Matriz de Correlación entre las Diferentes Variables', value=False)

# Crea un divisor para separar el dataframe de las gráficas.
st.divider()

# Histograma de precios.
if show_hist_price:
    # Carga el mensaje.
    st.write('***Histograma del promedio de precios de vehículos usados***')
    # Carga deslizador con el rango de precios.
    price_range = st.slider('Rango de Precios (USD)', 
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
    st.plotly_chart(fig1, use_container_width=True)
    # Crea divisor entre las gráficas.
    st.divider()


# Gráfica de dispersión kilometraje vs precio.
if show_scatter_km_price:
    # Carga el mensaje.
    st.write('***Gráfica de dispersión: kilometraje vs precio***')
    st.caption('Selecciona los diferentes filtros para ver más información sobre cómo afectan las condiciones el kilometraje y precio.')
    # Carga pills con filtros.
    vehicles_cond_km = vehicles['condition'].unique()
    selected_condition_km = st.pills("Filtros", 
                                     selection_mode="multi", 
                                     options=vehicles_cond_km, 
                                     default=['good', 'excellent'],
                                     key='km'
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
    st.plotly_chart(fig2, use_container_width=True)
    # Crea divisor entre las gráficas.
    st.divider()


# Gráfica de barras de precio por tipo de combustible.
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
        y_col = 'price'
        title = 'Precio Promedio por Tipo de Combustible'
    elif metric == 'Mediana':
        data = median_days = vehicles.groupby('fuel')['price'].median().reset_index()
        y_col = 'price'
        title= 'Precio Mediano por Tipo de Combustible'
    else:
        data = count_days = vehicles['fuel'].value_counts().reset_index()
        data.columns = ['fuel', 'counts']
        y_col = 'counts'
        title='Conteo de Vehículos por Tipo de Combustible'
    # Crea gráfica de barras.
    fig3 = px.bar(data, 
                  x='fuel', 
                  y='price',
                  title=title,
                  labels={'fuel': 'Tipo de Combustible', 'price': 'Precio (USD)' if y_col == 'price' else 'Cantidad de Vehículos'},
                  color='fuel'
                  )
    st.plotly_chart(fig3, use_container_width=True)
    # Crea divisor entre las gráficas.
    st.divider()


# Gráfica boxplot días en el mercado por condición.
if show_boxplot_days:
    # Carga el mensaje.
    st.write('***Gráfica de distribución de los días en el mercado por su condición***')
    st.caption('Modifíca los filtros para ver las diferentes condiciones')
    # Carga pills con filtros.
    vehicles_con_d = vehicles['condition'].unique()
    selected_condition_d = st.pills("Condiciones del Vehículo", 
                                    selection_mode="multi", 
                                    options=vehicles_con_d, 
                                    default=['good', 'excellent'],
                                    key='days'
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
                      color='condition',
                      color_discrete_sequence=px.colors.qualitative.Pastel1
                      )
    st.plotly_chart(fig4, use_container_width=True)
    # Crea divisor entre las graficas.
    st.divider()

# Matriz de correlación entre variables numéricas.
if show_corr:
    # Carga mensaje.
    st.write('***Matriz de correlación entre diferentes variables***')
    st.caption('Selecciona las variables a relacionar.')
    # Filtra los datos por columnas numericas y exluye 'is_4wd'.
    numeric_cols = vehicles.select_dtypes(include=['int64', 'float64']).columns.tolist()
    numeric_cols = [col for col in numeric_cols if col != 'is_4wd']
    # Carga multiselect con variables.
    selected_vars = st.multiselect("Variables",
                   options=numeric_cols,
                   default=['price', 'odometer', 'model_year']
                   )
    # Crea la correlación.
    if len(selected_vars) >= 2:
        corr_matrix = vehicles[selected_vars].corr().round(2)
    # Crea la gráfica.
    fig5 = px.imshow(corr_matrix,
                     x=selected_vars,
                     y=selected_vars,
                     title='Matriz de Correlación sobre Variables Numéricas', 
                     labels=dict(x='variable', y='variable', color='Correlación'),
                     color_continuous_scale='RdBu_r',
                     range_color=[-1, 1],
                     text_auto=True
                     )
    # Muestra el gráfico interactivo en la aplicación.
    st.plotly_chart(fig5, use_container_width=True)
