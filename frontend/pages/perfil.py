"""Profile page."""
import streamlit as st

st.set_page_config(page_title="Perfil", page_icon="👤")
st.title("👤 Perfil")
st.write("Informações do estudante.")
st.text_input("Nome")
st.text_input("Email")
st.button("Salvar")
