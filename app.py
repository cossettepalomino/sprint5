import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Sprint 5 : Comparativa de vehiculos para su venta") # encabezado

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button("Construir histograma")# crea boton para hitograma

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

build_dispersion = st.checkbox("Construir gráfico de dispersion")# crea boton para grafico de dispersion

if build_dispersion: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
                    
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig2, use_container_width=True)