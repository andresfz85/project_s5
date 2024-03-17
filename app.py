import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

print(car_data)

st.header("histograma")

build_histogram = st.checkbox('Construir un histograma') # crear un botón
        
if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button2 = st.button('Construir gráfico') # crear un botón
        
if hist_button2: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un gráfico
    fig2 = px.scatter(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)