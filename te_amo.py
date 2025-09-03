import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="💖 Mensaje para ti", page_icon="🌹", layout="centered")

# Animación de texto arcoíris
def texto_arcoiris(texto):
    colores = ["red", "orange", "yellow", "green", "blue", "purple"]
    resultado = ""
    for i, letra in enumerate(texto):
        resultado += f"<span style='color:{colores[i % len(colores)]}; font-size:90px; font-weight:bold;'>{letra}</span>"
    return resultado

# Mostrar título animado
st.markdown("<h1 style='text-align: center;'>💖 Para ti 💖</h1>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center;'>{texto_arcoiris('TE AMO')}</div>", unsafe_allow_html=True)

# Mostrar imágenes (más grandes y centradas)
st.image(r"C:\Users\Julio\Downloads\Pookie\Heart_PNG_Clipart-1003.png", caption="❤️ Mi corazón para ti", use_container_width=True)
st.image(r"C:\Users\Julio\Downloads\Pookie\Flower_PNG_Red_Transparent_Clipart.png", caption="🌹 Una flor especial", use_container_width=True)

# Mensaje final animado
mensaje = "Eres lo mejor que me ha pasado 💕"
for i in range(len(mensaje) + 1):
    st.markdown(f"<h3 style='text-align:center; color:magenta;'>{mensaje[:i]}</h3>", unsafe_allow_html=True)
    time.sleep(0.1)

