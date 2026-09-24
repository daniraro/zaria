"""Card components."""
import streamlit as st


def metric_card(label: str, value: str, delta: str = None):
    if delta:
        st.metric(label=label, value=value, delta=delta)
    else:
        st.metric(label=label, value=value)


def info_card(title: str, content: str):
    with st.container():
        st.subheader(title)
        st.write(content)
