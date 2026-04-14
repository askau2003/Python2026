# Streamlit app

import streamlit as st
import pandas as ps
import matplotlib.pyplot as plt

df = ps.read_csv('assets/Police_Department_Incident_Reports__2018_to_Present_20260414.csv')

selected_cat = st.sidebar.selectbox(
    "Select Crime Category",
    df["Incident Category"].unique()
)
selected_year = st.sidebar.selectbox(
    "Choose year",
    df["Incident Year"].unique()
)

filtered = df[
    (df["Incident Category"] == selected_cat) &
    (df["Incident Year"] == selected_year)
]

counts = filtered["Incident Category"].value_counts()

st.bar_chart(counts)