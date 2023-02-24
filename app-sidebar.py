import streamlit as st
import pandas as pd
import datetime

titanic_link = 'titanic.csv'

titanic_data = pd.read_csv(titanic_link)

st.title("Streamlit App - Sidebar")

sidebar = st.sidebar
sidebar.title("Esta es la barra lateral")
sidebar.write("Aqui van los elementos de entrada")

today = datetime.date.today()
today_date = st.date_input('Current date', today)

st.success('Current date: `%s`' % (today_date))

st.header("Informacion del conjunto de datos")
st.header("Descripción de los datos")

st.write("Este es un simple ejemplos de una app ...")
