# ==========================
# IMPORTING LIBRARIES
# ==========================
import streamlit as st
import pandas as pd
from PIL import Image
import io
import os
import tempfile
import speech_recognition as sr
from gtts import gTTS
import analysis
import visualization
import ai_helper

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
# HOME
# ==========================
if option == "Home":
    st.divider()
    st.subheader("Welcome to AI Data Analysis Assistant Pro! 🎉")
    st.markdown("### Features\n\n✅ Upload CSV Dataset\n\n✅ Auto-Generated AI Insights\n\n✅ AI Data Assistant with Voice\n\n✅ Voice Read-Aloud\n\n✅ Data Summary\n\n✅ Statistical Analysis\n\n✅ Interactive Plotly Visualizations")

# ==========================
# MAIN APP LOGIC (IF FILE UPLOADED)
# ==========================
if uploaded_file is not None: 
    try:
        bytes_data = uploaded_file.read()
        df = analysis.load_data(bytes_data)
        
        if df is None:
            st.warning("Could not read the CSV file. Please upload a valid file.")
            st.stop()
            
        df = analysis.clean_data(df) 
        
        summary = analysis.get_summary(df, uploaded_file.name) 
        filtered_df = df.copy() 
        
        if 'Released_Year' in filtered_df.columns: 
            years = pd.to_numeric(filtered_df['Released_Year'], errors='coerce').dropna() 
            if not years.empty: 
                min_yr, max_yr = int(years.min()), int(years.max()) 
                yr_range = st.sidebar.slider("Filter by Release Year", min_yr, max_yr, (min_yr, max_yr)) 
                
                numeric_years = pd.to_numeric(filtered_df['Released_Year'], errors='coerce')
                year_mask = (numeric_years >= yr_range[0]) & (numeric_years <= yr_range[1])
                filtered_df = filtered_df[year_mask] 
                
        filtered_summary = analysis.get_summary(filtered_df, uploaded_file.name)
        
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
        st.stop()

    # ==========================
    # AUTO INSIGHTS
    # ==========================
    if option == "AUTO GENERATE KEY INSIGHTS":
        st.divider()
        
        # FIX: Initialize session state for insights
        if 'insights' not in st.session_state:
            st.session_state.insights = None

        if st.button("✨ Auto-Generate Key Insights from Data"):
            with st.spinner("AI is scanning your dataset for Generating Key Insights..."):
                insight_question = "Analyze this dataset and give me exactly 3 key business insights or trends that a data analyst would find interesting. Keep each insight to 1-2 sentences."
                st.session_state.insights = ai_helper.ask_ai(insight_question, filtered_summary)
        
        # FIX: Move display and Read Aloud OUTSIDE the generate button block
        if st.session_state.insights:
            st.divider()            
            st.subheader("🔑 Key Insights")
            st.markdown(st.session_state.insights)
            
            if not st.session_state.insights.startswith("⚠️") and not st.session_state.insights.startswith("API Key missing"):
                if st.button("🔊 Read Insights Aloud", key="read_insights"):
                    with st.spinner("Generating audio..."):
                        tts = gTTS(text=st.session_state.insights, lang='en', slow=False)
                        mp3_fp = io.BytesIO()
                        tts.write_to_fp(mp3_fp)
                        st.audio(mp3_fp.getvalue(), format="audio/mp3")

    # ==========================
    # ASK AI
    # ==========================
    elif option == "Ask AI":
        st.header("🤖 Ask AI")
        
        # FIX: Initialize session state for answer
        if 'answer' not in st.session_state:
            st.session_state.answer = None
            
        # --- NATIVE SPEECH-TO-TEXT FEATURE ---
        audio_file = st.audio_input("🎤 Record your question")
        
        if audio_file:
            with st.spinner("Transcribing voice..."):
                bytes_data = audio_file.read()
                temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                temp_audio.write(bytes_data)
                temp_audio.close()
                
                recognizer = sr.Recognizer()
                try:
                    with sr.AudioFile(temp_audio.name) as source:
                        audio_data = recognizer.record(source)
                        transcribed_text = recognizer.recognize_google(audio_data)
                        st.success(f"Transcribed: {transcribed_text}")
                        st.session_state.question_text = transcribed_text
                        st.rerun() # Rerun to update the text box instantly
                except sr.UnknownValueError:
                    st.error("Could not understand audio. Please try again.")
                except sr.RequestError:
                    st.error("Speech recognition service error. Check internet connection.")
                finally:
                    os.unlink(temp_audio.name)

        question = st.text_input("✨Ask about your dataset", key="question_text")
        
        if st.button("Get Answer"):
            if question.strip() == "":
                st.warning("Enter a question or record your voice")
            else:
                with st.spinner("AI analyzing..."):
                    st.session_state.answer = ai_helper.ask_ai(question, filtered_summary)
        
        # FIX: Move display and Read Aloud OUTSIDE the get answer button block
        if st.session_state.answer:
            st.markdown(st.session_state.answer)
            
            if not st.session_state.answer.startswith("⚠️") and not st.session_state.answer.startswith("API Key missing"):
                if st.button("🔊 Read Answer Aloud", key="read_answer"):
                    with st.spinner("Generating audio..."):
                        tts = gTTS(text=st.session_state.answer, lang='en', slow=False)
                        mp3_fp = io.BytesIO()
                        tts.write_to_fp(mp3_fp)
                        st.audio(mp3_fp.getvalue(), format="audio/mp3")

    # ==========================
    # SUMMARY
    # ==========================
    elif option == "Dataset Summary":
        st.divider()
        st.header("📊 Dataset Summary")
        c1, c2, c3 = st.columns(3)
        c1.metric("Rows", filtered_df.shape[0])
        c2.metric("Columns", filtered_df.shape[1])
        c3.metric("Missing Values", int(filtered_df.isnull().sum().sum()))
        st.divider()
        st.subheader("Preview")
        st.dataframe(filtered_df.head(10), use_container_width=True)
        st.divider()
        st.subheader("Column Names")
        st.write(list(filtered_df.columns))
        st.divider()
        st.subheader("Data Types")
        st.dataframe(filtered_df.dtypes.astype(str))
        st.divider()
        st.subheader("Missing Values")
        st.dataframe(filtered_df.isnull().sum())

    # ==========================
    # STATISTICS 
    # ==========================
    elif option == "Statistics":
        st.header("📈 Statistics")
        stats = analysis.get_numeric_stats(filtered_df)
        if stats is not None:
            st.dataframe(stats)
        else:
            st.warning("No numeric columns")
            
        st.divider()        
        categorical = filtered_df.select_dtypes(include="object")
        if len(categorical.columns):
            col = st.selectbox("Select Category", categorical.columns)
            counts_df = analysis.get_category_counts(filtered_df, col)
            
            if counts_df is not None:
                st.dataframe(
                    counts_df,
                    column_config={
                        "Count": st.column_config.Column(alignment="center"),
                        col: st.column_config.Column(alignment="center")
                    },
                    use_container_width=True  
                )

    # ==========================
    # VISUALIZATION 
    # ==========================
    elif option == "Visualization":
        st.header("📊 Interactive Visualization")
        
        chart_type = st.selectbox("Choose Chart", ["Bar Chart", "Histogram", "Pie Chart", "Scatter Plot"])
        fig = None

        if chart_type == "Bar Chart":
            cols = filtered_df.select_dtypes(include="object").columns
            if len(cols):
                col = st.selectbox("Category", cols)
                fig = visualization.plot_bar(filtered_df, col)

        elif chart_type == "Histogram":
            cols = filtered_df.select_dtypes(include="number").columns
            if len(cols):
                col = st.selectbox("Numeric Column", cols)
                fig = visualization.plot_histogram(filtered_df, col)

        elif chart_type == "Pie Chart":
            cols = filtered_df.select_dtypes(include="object").columns
            if len(cols):
                col = st.selectbox("Category", cols)
                fig = visualization.plot_pie(filtered_df, col)

        elif chart_type == "Scatter Plot":
            cols = filtered_df.select_dtypes(include="number").columns
            if len(cols) >= 2:
                x = st.selectbox("X Axis", cols)
                y = st.selectbox("Y Axis", cols, index=1)
                fig = visualization.plot_scatter(filtered_df, x, y)

        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)

else:
    if option != "Home":
        st.warning("Please upload a CSV file from the sidebar to use this feature.")
