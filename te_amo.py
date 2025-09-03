import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="💖 Mensaje para ti", page_icon="🌹", layout="centered")

# --- Estilos (fondo suave y animaciones) ---
st.markdown("""
<style>
body {
  background: radial-gradient(circle at 20% 20%, #ffe6f2 0%, #ffffff 40%) no-repeat fixed;
}
.pulse {
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0% { transform: scale(1); filter: drop-shadow(0 0 0px rgba(255,0,102,.2)); }
  50% { transform: scale(1.03); filter: drop-shadow(0 0 10px rgba(255,0,
