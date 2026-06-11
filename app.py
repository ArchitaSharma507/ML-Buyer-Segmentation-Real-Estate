import streamlit as st
import pandas as pd

st.title("Buyer Segmentation Dashboard")

# Load data
df = pd.read_excel("ML_DATASET.FINAL.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")
