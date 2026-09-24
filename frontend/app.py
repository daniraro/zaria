"""Frontend application entry point."""
import streamlit as st

st.set_page_config(page_title="Zaria", page_icon="🎓", layout="wide")
st.title("Zaria - Plataforma de Diagnóstico Educacional")
st.write("Bem-vindo ao Zaria!")

page = st.sidebar.selectbox("Navegação", ["Dashboard", "Diagnóstico", "Desempenho", "Perfil"])

if page == "Dashboard":
    st.info("Página Dashboard - Em desenvolvimento")
elif page == "Diagnóstico":
    st.info("Página Diagnóstico - Em desenvolvimento")
elif page == "Desempenho":
    st.info("Página Desempenho - Em desenvolvimento")
elif page == "Perfil":
    st.info("Página Perfil - Em desenvolvimento")
