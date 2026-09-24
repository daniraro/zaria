"""Chart components."""
import streamlit as st
import pandas as pd


def performance_chart(data: pd.DataFrame):
    st.line_chart(data)


def subject_breakdown_chart(data: pd.DataFrame):
    st.bar_chart(data)
