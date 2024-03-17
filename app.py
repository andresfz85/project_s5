import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

print(car_data)

st.header("histograma")

build_histogram = st.checkbox('Histograma odometer') # crear un botón
        
if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    #mostrar comentarios
    st.write("Comentario: Los autos que marcan entre 100 k y 120k en el odómetro son más vendidos frecuentemente")

hist_button2 = st.button('Dispersión: Odometer vs price') # crear un botón
        
if hist_button2: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Ver Gráfico de dispersión km recorrido vs precio')
            
    # crear un gráfico
    fig2 = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

    #mostrar comentarios
    st.write("Comentario: Salvo valores atípicos, el precio disminuye mientra más tiene más recorrido")

hist_button3 = st.button('Dispersión: Model_year vs price') # crear un botón

if hist_button3: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión año de modelo vs precio')
            
    # crear un gráfico
    fig3 = px.scatter(car_data, x="model_year", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)

    #mostrar comentarios
    st.write("Comentario: Salvo valores atípicos, el precio tiende a aumentar en modelos más nuevos")