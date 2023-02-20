import streamlit as st

st.title('Streamlit - App Welcome')


def bienvenida(nombre):
    mymensaje = "Bienvenido" + nombre
    return mymensaje


myname = st.text_input('nombre: ')

if (myname):
    mensaje = bienvenida(myname)
    st.write(f" Resultado : {mensaje}")
