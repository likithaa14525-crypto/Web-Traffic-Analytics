import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.title("📊 Web Traffic Analytics Dashboard")

st.subheader("Page Views")
st.bar_chart(df["page"].value_counts())

st.subheader("Session Time")
st.line_chart(df["session_time"])

st.subheader("Key Metrics")
st.write("Average Session Time:", df["session_time"].mean())
st.write("Drop-off Rate:", (df["exit"] == "Yes").mean() * 100, "%")