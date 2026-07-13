# ==========================
# IMPORTING LIBRARIES
# ==========================
import streamlit as st
import pandas as pd
from PIL import Image
import analysis
import visualization
import ai_helper
import voice_helper

# ==========================
# PAGE SETTINGS
# ==========================
st.set_page_config(page_title="AI Data Analysis Assistant", page_icon="🤖", layout="wide")
st.title("🤖 AI Data Analysis Assistant Pro")
st.write("Upload CSV files, analyze data, create interactive charts and ask AI questions.")

try:
    img = Image.open("Sylani.png")
    rotated_img = img.rotate(25, expand=True)
    st.image(rotated_img, width=200)
except FileNotFoundError:
    pass

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select One", ["Home", "AUTO GENERATE KEY INSIGHTS", "Ask AI", "Dataset Summary", "Statistics", "Visualization"])
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# ==========================
# SESSION STATE (persistence across reruns)
# ==========================
if "insights" not in st.session_state:
    st.session_state.insights = None
if "ai_answer" not in st.session_state:
    st.session_state.ai_answer = None

# ==========================
# HOME
# ==========================
if option == "Home":
    st.divider()
    st.subheader("Welcome to AI Data Analysis Assistant Pro! 🎉")
    st.markdown("### Features\n\n✅ Upload CSV Dataset\n\n✅ Auto-Generated AI Insights\n\n✅ AI Data Assistant with Voice\n\n✅ Data Summary with Voice\n\n✅ Statistical Analysis\n\n✅ Interactive Plotly Visualizations")
    st.divider()

    if st.button("🔊 Listen to Welcome Message"):
        welcome_text = "Welcome to AI Data Analysis Assistant Pro. Upload a CSV file to get started with automated insights, interactive visualizations, and AI-powered answers."
        with st.spinner("Generating voice..."):
            audio_bytes = voice_helper.text_to_speech(welcome_text)
        st.audio(audio_bytes, format="audio/mp3")

# ==========================
# MAIN APP LOGIC (IF FILE UPLOADED)
# ==========================
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
            year_mask = (numeric_years >= yr_range[0]) & (numeric_years <= yr_range[1])
            filtered_df = filtered_df[year_mask]

    # Use filtered summary so AI reflects the active filter
    filtered_summary = analysis.get_summary(filtered_df, uploaded_file.name)

    # ==========================
    # AUTO INSIGHTS
    # ==========================
    if option == "AUTO GENERATE KEY INSIGHTS":
        st.divider()
        if st.button("✨ Auto-Generate Key Insights from Data"):
            with st.spinner("AI is scanning your dataset for Generating Key Insights..."):
                insight_question = "Analyze this dataset and give me exactly 3 key business insights or trends that a data analyst would find interesting. Keep each insight to 1-2 sentences."
                st
