import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Marketing Campaign Analysis",
    layout="wide"
)

st.title("📊 Marketing Campaign Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload marketing_cleaned.csv",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Customers",
            len(df)
        )

    with col2:
        st.metric(
            "Average Income",
            round(df["Income"].mean(), 2)
        )

    with col3:
        st.metric(
            "Average Spend",
            round(df["Total_Spend"].mean(), 2)
        )

    st.subheader("Income Distribution")
    st.bar_chart(df["Income"])

    st.subheader("Total
