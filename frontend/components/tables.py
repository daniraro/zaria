import streamlit as st
import pandas as pd


def data_table(data: pd.DataFrame, title: str = None):
    if title:
        st.subheader(title)
    st.dataframe(data, use_container_width=True)


def sortable_table(data: pd.DataFrame, sort_by: str = None):
    if sort_by:
        data = data.sort_values(by=sort_by, ascending=False)
    st.dataframe(data, use_container_width=True)
