import streamlit as st
st.title("Aplicacion en Streamlit")
st.sidebar.title("parametros")
valor = st.sidebar.slider("seleccione un valor", 0, 10, 3)
st.write("El resultado elevado al cuadrado es:", valor ** 2)