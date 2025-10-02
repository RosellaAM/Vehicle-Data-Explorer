import pandas as pd
import plotly.express as px
import streamlit as st

# Load vehicle dataset
vehicles = pd.read_csv("vehicles_us.csv")
if vehicles is None or vehicles.empty:
    st.write('Dataset is empty or could not be loaded')
else:
    # Application header
    st.title('Used Car Market Analysis')

    # Data preview section
    st.subheader('Dataset Preview')
    st.dataframe(vehicles.sample(10))
    full_data = st.button('Show Complete Dataset')
    if full_data:
        with st.expander('Complete Data View'):
            # Show full dataset (500 row limit)
            st.dataframe(vehicles.head(500))

    # Visualization selection options
    show_hist_price = st.checkbox('Display Price Distribution Histogram', value=False)
    show_scatter_km_price = st.checkbox('Display Mileage vs Price Scatter Chart', value=False)  
    show_bar_fuel = st.checkbox('Display Fuel Type Price Comparison', value=False)        
    show_boxplot_days = st.checkbox('Display Market Duration by Vehicle Condition', value=False)
    show_corr = st.checkbox('Display Variable Correlation Matrix', value=False)

    # Section separator
    st.divider()

    # Price distribution analysis
    if show_hist_price:
        st.write('***Used Vehicle Price Distribution Analysis***')
        # Price range selector
        price_range = st.slider('Select Price Range (USD)', 
                                min_value= int(vehicles['price'].min()), 
                                max_value= int(vehicles['price'].max()),
                                value=(5000, 50000))
        # Apply price filters
        vehicles_price_filt = vehicles[(vehicles['price'] >= price_range[0]) & (vehicles['price'] <= price_range[1])]
        # Generate histogram
        fig1= px.histogram(vehicles_price_filt,
                        x='price', 
                        nbins=50, 
                        title='Vehicle Price Distribution Analysis', 
                        labels={'price' : 'Price (USD)'}, 
                        color_discrete_sequence=['purple']
                        )
        st.plotly_chart(fig1, use_container_width=True)
        st.divider()

    # Mileage-price relationship
    if show_scatter_km_price:
        st.write('***Mileage vs Price Correlation***')
        st.caption('Apply condition filters to analyze how vehicle status affects pricing and mileage.')
        # Condition filters
        vehicles_cond_km = vehicles['condition'].unique()
        selected_condition_km = st.pills("Condition Filters", 
                                        selection_mode="multi", 
                                        options=vehicles_cond_km, 
                                        default=['good', 'excellent'],
                                        key='km'
                                        )
        # Filter by selected conditions
        filtered_vehicles_by_con = vehicles[vehicles['condition'].isin(selected_condition_km)]
        # Generate scatter plot
        if len(filtered_vehicles_by_con) == 0:
            st.warning('No vehicles match the selected criteria.')
        else:
            fig2 = px.scatter(filtered_vehicles_by_con, 
                            x='odometer',
                            y='price',
                            color='condition',
                            title='Price vs Mileage Analysis',
                            labels={'odometer': 'Mileage', 'price': 'Price (USD)'},
                            trendline='lowess'
                            )
            st.plotly_chart(fig2, use_container_width=True)
        st.divider()

    # Fuel type analysis
    if show_bar_fuel:
        st.write('***Fuel Type Price Analysis***')
        st.caption('Choose your analysis metric for fuel type comparison.')
        # Metric selection
        metric = st.selectbox("Select Analysis Metric", 
                            options=['Average Price', 'Median Price', 'Inventory Count']
                            )
        if metric == 'Average Price':
            data = vehicles.groupby('fuel')['price'].mean().reset_index()
            y_col = 'price'
            title = 'Average Vehicle Price by Fuel Type'
        elif metric == 'Median Price':
            data = vehicles.groupby('fuel')['price'].median().reset_index()
            y_col = 'price'
            title= 'Median Vehicle Price by Fuel Type'
        else:
            data = vehicles['fuel'].value_counts().reset_index()
            data.columns = ['fuel', 'counts']
            y_col = 'counts'
            title='Vehicle Inventory by Fuel Type'
        # Generate bar chart
        fig3 = px.bar(data, 
                    x='fuel', 
                    y=y_col,
                    title=title,
                    labels={'fuel': 'Fuel Type', y_col: 'Price (USD)' if y_col == 'price' else 'Vehicle Count'},
                    color='fuel'
                    )
        st.plotly_chart(fig3, use_container_width=True)
        st.divider()

    # Market duration analysis
    if show_boxplot_days:
        st.write('***Market Duration by Vehicle Condition***')
        st.caption('Filter by vehicle condition to analyze market duration patterns.')
        # Condition selection
        vehicles_con_d = vehicles['condition'].unique()
        selected_condition_d = st.pills("Select Vehicle Conditions", 
                                        selection_mode="multi", 
                                        options=vehicles_con_d, 
                                        default=['good', 'excellent'],
                                        key='days'
                                        )
        # Apply condition filters
        filtered_data_by_con_d = vehicles[vehicles['condition'].isin(selected_condition_d)]
        # Generate boxplot
        if len(filtered_data_by_con_d) == 0:
            st.warning('No data matches the selected conditions.')
        else:
            fig4 = px.box(filtered_data_by_con_d,
                        x='condition',
                        y='days_listed',
                        title='Market Duration Analysis by Vehicle Condition',
                        labels={'condition': 'Vehicle Condition', 'days_listed': 'Days on Market'},
                        color='condition',
                        color_discrete_sequence=px.colors.qualitative.Pastel1
                        )
            st.plotly_chart(fig4, use_container_width=True)
        st.divider()

    # Correlation analysis
    if show_corr:
        st.write('***Variable Correlation Analysis***')
        st.caption('Select numeric variables to analyze their relationships.')
        # Get numeric columns
        numeric_cols = vehicles.select_dtypes(include=['int64', 'float64']).columns.tolist()
        numeric_cols = [col for col in numeric_cols if col != 'is_4wd']
        # Variable selection
        selected_vars = st.multiselect("Select Variables for Correlation",
                    options=numeric_cols,
                    default=['price', 'odometer', 'model_year']
                    )
        # Calculate correlations
        if len(selected_vars) >= 2:
            corr_matrix = vehicles[selected_vars].corr().round(2)
        # Generate correlation matrix
        fig5 = px.imshow(corr_matrix,
                        x=selected_vars,
                        y=selected_vars,
                        title='Numeric Variables Correlation Matrix', 
                        labels=dict(x='Variables', y='Variables', color='Correlation Strength'),
                        color_continuous_scale='RdBu_r',
                        range_color=[-1, 1],
                        text_auto=True
                        )
        # Display correlation matrix
        st.plotly_chart(fig5, use_container_width=True)