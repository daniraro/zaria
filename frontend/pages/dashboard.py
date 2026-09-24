"""Dashboard page."""
import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊")
st.title("📊 Dashboard")
st.write("Visão geral do desempenho do estudante.")
st.metric(label="Média Geral", value="0.0")
st.metric(label="Questões Respondidas", value="0")
st.metric(label="Taxa de Acerto", value="0%")
