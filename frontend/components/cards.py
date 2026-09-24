import streamlit as st


def metric_card(label: str, value: str, delta: str = None):
    col = st.columns(1)[0]
    with col:
        st.metric(label=label, value=value, delta=delta)


def info_card(title: str, content: str):
    with st.expander(title):
        st.write(content)
