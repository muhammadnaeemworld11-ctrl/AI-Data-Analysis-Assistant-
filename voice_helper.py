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


# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select One", ["Home", "AUTO Generate Key Insides", "Ask AI Data Assistant with Voice or Chat ", "Data Summary With ai voice", "StatisticsWith Voice ", "Visualization"])
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"]) 

# ==========================
# HOME
# ==========================
if option == "Home":
    st.divider()
    st.subheader("Welcome to AI Data Analysis Assistant Pro! 🎉")
    st.markdown("### Features\n\n✅ Upload CSV Dataset\n\n✅ AUTO Generate Key Insides \n\n✅ Ask AI Data Assistant with Voice or Chat\n\n✅ Data Summary with ai Voice\n\n✅ Statistical Analysis With Voice\n\n✅ Interactive Plotly Visualizations")
    st.divider()
    
try:
    img = Image.open("Blind_people.jpg") 
except FileNotFoundError:
    pass
    # 🔊 Welcome Voice Message
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
    # AUTO Generate Key Insides
    # ==========================
    if option == "AUTO Generate Key Insides":
        st.divider()
        if st.button("✨ Auto-Generate Key Insights from Data"):
            with st.spinner("AI is scanning your dataset for Generating Key Insights..."):
                insight_question = "Analyze this dataset and give me exactly 3 key business insights or trends that a data analyst would find interesting. Keep each insight to 1-2 sentences."
                insights = ai_helper.ask_ai(insight_question, summary)
                st.divider()            
            st.subheader("🔑 Key Insights")
            st.markdown(insights)

            # 🔊 Speak the insights
            st.divider()
            if st.button("🔊 Listen to Insights"):
                with st.spinner("Generating voice..."):
                    audio_bytes = voice_helper.text_to_speech(insights)
                st.audio(audio_bytes, format="audio/mp3")

    # ==========================
    # ASK AI
    # ==========================
    elif option == "Ask AI":
        st.header("🤖 Ask AI")
        question = st.text_input("✨Ask about your dataset")
        if st.button("Get Answer"):
            if question.strip() == "":
                st.warning("Enter a question")
            else:
                with st.spinner("AI analyzing..."):
                    answer = ai_helper.ask_ai(question, summary)
                st.markdown(answer)

                # 🔊 Speak the answer
                st.divider()
                if st.button("🔊 Listen to Answer"):
                    with st.spinner("Generating voice..."):
                        audio_bytes = voice_helper.text_to_speech(answer)
                    st.audio(audio_bytes, format="audio/mp3")

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
        
        # 🔊 Voice Summary Button
        st.divider()
        if st.button("🔊 Listen to Dataset Summary"):
            voice_text = (
                f"This dataset contains {filtered_df.shape[0]} rows "
                f"and {filtered_df.shape[1]} columns. "
                f"There are {int(filtered_df.isnull().sum().sum())} missing values. "
                f"The columns in this dataset are: {', '.join(filtered_df.columns)}. "
            )
            numeric_cols = filtered_df.select_dtypes(include='number').columns
            if len(numeric_cols) > 0:
                voice_text += "Here are some key statistics. "
                for col in numeric_cols[:5]:
                    mean_val = filtered_df[col].mean()
                    voice_text += f"The average {col} is {mean_val:.2f}. "

            with st.spinner("Generating voice..."):
                audio_bytes = voice_helper.text_to_speech(voice_text)
            st.audio(audio_bytes, format="audio/mp3")

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

            # 🔊 Speak statistics
            if st.button("🔊 Listen to Statistics"):
                voice_text = "Here are the key statistics for numeric columns. "
                for col in stats.columns:
                    voice_text += f"For {col}, "
                    voice_text += f"the mean is {stats.loc['mean', col]:.2f}, "
                    voice_text += f"the minimum is {stats.loc['min', col]:.2f}, "
                    voice_text += f"and the maximum is {stats.loc['max', col]:.2f}. "
                with st.spinner("Generating voice..."):
                    audio_bytes = voice_helper.text_to_speech(voice_text)
                st.audio(audio_bytes, format="audio/mp3")
        else:
            st.warning("No numeric columns")
            
        st.divider()        
        categorical = filtered_df.select_dtypes(include="object")
        if len(categorical.columns):
            col = st.selectbox("Select Category", categorical.columns)
            counts_df = analysis.get_category_counts(filtered_df, col)
            
            # Convert Series to DataFrame for better display
            counts_df = counts_df.reset_index()
            counts_df.columns = [col, "Count"]
            
            st.dataframe(counts_df, use_container_width=True)

    # ==========================
    # VISUALIZATION 
    # ==========================
    elif option == "Visualization":
        st.header("📊

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select One", ["Home", "Auto Generate Insides", "Ask AI", "Dataset Summary", "Statistics", "Visualization"])
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"]) 

# ==========================
# HOME
# ==========================
if option == "Home":
    st.divider()
    st.subheader("Welcome to AI Data Analysis Assistant Pro! 🎉")
    st.markdown("### Features\n\n✅ Upload CSV Dataset\n\n✅ Auto-Generated AI Insights\n\n✅ AI Data Assistant with Voice\n\n✅ Data Summary with Voice\n\n✅ Statistical Analysis\n\n✅ Interactive Plotly Visualizations")
    st.divider()
    
    # 🔊 Welcome Voice Message
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

            # 🔊 Speak the insights
            st.divider()
            if st.button("🔊 Listen to Insights"):
                with st.spinner("Generating voice..."):
                    audio_bytes = voice_helper.text_to_speech(insights)
                st.audio(audio_bytes, format="audio/mp3")

    # ==========================
    # ASK AI
    # ==========================
    elif option == "Ask AI":
        st.header("🤖 Ask AI")
        question = st.text_input("✨Ask about your dataset")
        if st.button("Get Answer"):
            if question.strip() == "":
                st.warning("Enter a question")
            else:
                with st.spinner("AI analyzing..."):
                    answer = ai_helper.ask_ai(question, summary)
                st.markdown(answer)

                # 🔊 Speak the answer
                st.divider()
                if st.button("🔊 Listen to Answer"):
                    with st.spinner("Generating voice..."):
                        audio_bytes = voice_helper.text_to_speech(answer)
                    st.audio(audio_bytes, format="audio/mp3")

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
        
        # 🔊 Voice Summary Button
        st.divider()
        if st.button("🔊 Listen to Dataset Summary"):
            voice_text = (
                f"This dataset contains {filtered_df.shape[0]} rows "
                f"and {filtered_df.shape[1]} columns. "
                f"There are {int(filtered_df.isnull().sum().sum())} missing values. "
                f"The columns in this dataset are: {', '.join(filtered_df.columns)}. "
            )
            numeric_cols = filtered_df.select_dtypes(include='number').columns
            if len(numeric_cols) > 0:
                voice_text += "Here are some key statistics. "
                for col in numeric_cols[:5]:
                    mean_val = filtered_df[col].mean()
                    voice_text += f"The average {col} is {mean_val:.2f}. "

            with st.spinner("Generating voice..."):
                audio_bytes = voice_helper.text_to_speech(voice_text)
            st.audio(audio_bytes, format="audio/mp3")

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

            # 🔊 Speak statistics
            if st.button("🔊 Listen to Statistics"):
                voice_text = "Here are the key statistics for numeric columns. "
                for col in stats.columns:
                    voice_text += f"For {col}, "
                    voice_text += f"the mean is {stats.loc['mean', col]:.2f}, "
                    voice_text += f"the minimum is {stats.loc['min', col]:.2f}, "
                    voice_text += f"and the maximum is {stats.loc['max', col]:.2f}. "
                with st.spinner("Generating voice..."):
                    audio_bytes = voice_helper.text_to_speech(voice_text)
                st.audio(audio_bytes, format="audio/mp3")
        else:
            st.warning("No numeric columns")
            
        st.divider()        
        categorical = filtered_df.select_dtypes(include="object")
        if len(categorical.columns):
            col = st.selectbox("Select Category", categorical.columns)
            counts_df = analysis.get_category_counts(filtered_df, col)
            
            # Convert Series to DataFrame for better display
            counts_df = counts_df.reset_index()
            counts_df.columns = [col, "Count"]
            
            st.dataframe(counts_df, use_container_width=True)

    # ==========================
    # VISUALIZATION 
    # ==========================
    elif option == "Visualization":
        st.header("📊
