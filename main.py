import streamlit as st
import pandas as pd
import analysis
import visualization
import ai_helper
import voice_helper

st.set_page_config(page_title="AI Data Analysis Assistant", page_icon="🤖", layout="wide")
st.title("🤖 AI Data Analysis Assistant Pro")

st.sidebar.title("Navigation")
option = st.sidebar.radio("Select One", ["Home", "AUTO GENERATE KEY INSIGHTS", "Ask AI", "Dataset Summary", "Statistics", "Visualization"])
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if option == "Home":
    st.write("Welcome! Upload a CSV to begin.")

if uploaded_file is not None:
    df = analysis.load_data(uploaded_file).copy()
    df = analysis.clean_data(df)
    summary = analysis.get_summary(df, uploaded_file.name)
    filtered_df = df.copy()

    if "Released_Year" in filtered_df.columns:
        years = pd.to_numeric(filtered_df["Released_Year"], errors="coerce").dropna()
        if not years.empty:
            min_yr, max_yr = int(years.min()), int(years.max())
            yr_range = st.sidebar.slider("Filter by Release Year", min_yr, max_yr, (min_yr, max_yr))
            numeric_years = pd.to_numeric(filtered_df["Released_Year"], errors="coerce")
            filtered_df = filtered_df[(numeric_years >= yr_range[0]) & (numeric_years <= yr_range[1])]

    if option == "AUTO GENERATE KEY INSIGHTS":
        if st.button("Generate Insights"):
            st.write(ai_helper.ask_ai("Give 3 key insights", summary))
            
    elif option == "Ask AI":
        q = st.text_input("Question")
        if st.button("Ask"):
            st.write(ai_helper.ask_ai(q, summary))

    elif option == "Dataset Summary":
        st.dataframe(filtered_df.head())

    elif option == "Statistics":
        st.dataframe(analysis.get_numeric_stats(filtered_df))

    elif option == "Visualization":
        st.write("Visualization goes here")
