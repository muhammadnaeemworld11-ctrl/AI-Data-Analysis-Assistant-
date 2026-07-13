# ==========================
# IMPORTING LIBRARIES
# ==========================
import streamlit as st
import pandas as pd
from PIL import Image
import analysis
import visualization
import ai_helper
import io
from gtts import gTTS
import speech_recognition as sr

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
option = st.sidebar.radio("Select One", ["Home", "AUTO GENERATE KEY INSIGHTS", "Voice AI Summary", "Ask AI", "Dataset Summary", "Statistics", "Visualization"])
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"]) 

# ==========================
# HOME
# ==========================
if option == "Home":
    st.divider()
    st.subheader("Welcome to AI Data Analysis Assistant Pro! 🎉")
    st.markdown("### Features\n\n✅ Upload CSV Dataset\n\n✅ Auto-Generated AI Insights\n\n✅ AI Data Assistant\n\n✅ Voice AI Summary\n\n✅ Voice Question Input\n\n✅ Data Summary\n\n✅ Statistical Analysis\n\n✅ Interactive Plotly Visualizations")

# ==========================
# MAIN APP LOGIC (IF FILE UPLOADED)
# ==========================
if uploaded_file is not None: 
    df = analysis.load_data(uploaded_file).copy() 
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

    # ==========================
    # AUTO INSIGHTS
    # ==========================
    if option == "AUTO GENERATE KEY INSIGHTS":
        st.divider()
        if st.button("✨ Auto-Generate Key Insights from Data"):
            with st.spinner("AI is scanning your dataset for Generating Key Insights..."):
                insight_question = "Analyze this dataset and give me exactly 3 key business insights or trends that a data analyst would find interesting. Keep each insight to 1-2 sentences."
                insights = ai_helper.ask_ai(insight_question, summary)
                st.divider()            
            st.subheader("🔑 Key Insights")
            st.markdown(insights)

    # ==========================
    # VOICE AI SUMMARY
    # ==========================
    elif option == "Voice AI Summary":
        st.divider()
        st.header("🎙️ Voice AI Summary")
        st.write("Click the button below to have the AI generate a short summary of your dataset and read it out loud.")
        
        if st.button("🔊 Generate & Play Voice Summary"):
            with st.spinner("AI is analyzing the data and generating voice..."):
                voice_question = "Provide a very brief, 3-sentence spoken summary of this dataset's key statistics and purpose. Keep it conversational."
                text_answer = ai_helper.ask_ai(voice_question, summary)
                
                st.subheader("AI Text Summary:")
                st.markdown(text_answer)
                
                try:
                    st.info("Generating audio file...")
                    audio_bytes = io.BytesIO()
                    tts = gTTS(text=text_answer, lang='en', slow=False)
                    tts.write_to_fp(audio_bytes)
                    audio_bytes.seek(0)
                    
                    st.success("Audio ready! Play it below:")
                    st.audio(audio_bytes, format='audio/mp3')
                except Exception as e:
                    st.error(f"Voice Error: {e}. The AI response might have been too long or contained characters that can't be read.")

    # ==========================
    # ASK AI (WITH VOICE INPUT)
    # ==========================
    elif option == "Ask AI":
        st.header("🤖 Ask AI")
        st.write("Type your question below, or click the microphone icon to speak it.")
        
        # Initialize default question text
        question_text = ""

        # Microphone Input Button
        audio_bytes = st.audio_input("🎤 Click to record your question")
        
        if audio_bytes is not None:
            st.info("Transcribing your voice...")
            try:
                # Read the recorded audio bytes
                audio_data = audio_bytes.read()
                
                # Use SpeechRecognition to transcribe
                recognizer = sr.Recognizer()
                audio_file = sr.AudioFile(io.BytesIO(audio_data))
                
                with audio_file as source:
                    audio_record = recognizer.record(source)
                    
                # Convert speech to text using Google's free API
                question_text = recognizer.recognize_google(audio_record)
                st.success(f"Heard: {question_text}")
            except Exception as e:
                st.error(f"Could not understand audio: {e}")

        # Text Input Box (auto-fills with your voice transcription if available)
        question = st.text_input("✨Ask about your dataset", value=question_text)
        
        if st.button("Get Answer"):
            if question.strip() == "":
                st.warning("Enter a question")
            else:
                with st.spinner("AI analyzing..."):
                    answer = ai_helper.ask_ai(question, summary)
                st.markdown(answer)

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
            st.dataframe(
                counts_df,
                column_config={
                    "count": st.column_config.Column(alignment="center"),
                    col: st.column_config.Column(alignment="center")
                },
                use_container_width=True
