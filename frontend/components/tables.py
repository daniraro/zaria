"""Table components."""
import streamlit as st
import pandas as pd


def questions_table(data: pd.DataFrame):
    st.dataframe(data, use_container_width=True)


def results_table(data: pd.DataFrame):
    st.dataframe(data, use_container_width=True)
