import streamlit as st
from pages import dashboard, diagnostico, desempenho, perfil

st.set_page_config(page_title="Zaria", page_icon="📚", layout="wide")

st.title("Zaria - Plataforma de Diagnóstico Educacional")

menu = st.sidebar.selectbox(
    "Menu",
    ["Dashboard", "Diagnóstico", "Desempenho", "Perfil"]
)

if menu == "Dashboard":
    dashboard.show()
elif menu == "Diagnóstico":
    diagnostico.show()
elif menu == "Desempenho":
    desempenho.show()
elif menu == "Perfil":
    perfil.show()
