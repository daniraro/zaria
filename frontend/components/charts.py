import streamlit as st
import pandas as pd


def bar_chart(data: pd.DataFrame, x: str, y: str, title: str = None):
    st.bar_chart(data.set_index(x)[y])
    if title:
        st.caption(title)


def line_chart(data: pd.DataFrame, x: str, y: str, title: str = None):
    st.line_chart(data.set_index(x)[y])
    if title:
        st.caption(title)
