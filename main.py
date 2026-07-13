import streamlit as st
import pandas as pd

# LAZY IMPORTS
import analysis
import visualization
import ai_helper

# ==========================
# PAGE SETTINGS
# ==========================
st.set_page_config(page_title="AI Data Analysis Assistant", page_icon="🤖", layout="wide")
st.title("🤖 AI Data Analysis Assistant Pro")
st.write("Upload CSV files, analyze data, create interactive charts and ask AI questions.")
st.divider()

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select", ["Home", "Dataset Summary", "Statistics", "Visualization", "Ask AI"])
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# ==========================
# HOME
# ==========================
if option == "Home":
    st.subheader("Welcome")
    st.markdown("### Features\n\n✅ Upload CSV Dataset\n\n✅ AI Smart Natural Language Filtering\n\n✅ Auto-Generated AI Insights\n\n✅ Statistical Analysis\n\n✅ Interactive Plotly Visualizations\n\n✅ AI Data Assistant\n\n✅ Export to PDF")

# ==========================
# LOAD & CLEAN DATA
# ==========================
if uploaded_file is not None:
    df = analysis.load_data(uploaded_file)
    df = analysis.clean_data(df)

    # ==========================
    # SIDEBAR AI SMART FILTER
    # ==========================
    st.sidebar.divider()
    st.sidebar.subheader("🤖 AI Smart Filter")
    
    if "filter_query" not in st.session_state:
        st.session_state.filter_query = None

    ai_filter_input = st.sidebar.text_input(
        "Filter data in plain English:", 
        placeholder="e.g., Movies after 2000 with rating > 8.5"
    )
    
    if st.sidebar.button("Apply AI Filter"):
        if ai_filter_input.strip():
            with st.sidebar.spinner("AI is writing filter code..."):
                query_string = ai_helper.get_ai_filter(ai_filter_input, list(df.columns))
                
            if query_string:
                st.session_state.filter_query = query_string
                st.sidebar.success(f"AI Generated Code: `{query_string}`")
            else:
                st.sidebar.warning("AI couldn't understand that filter. Showing all data.")
                st.session_state.filter_query = None
        else:
            st.sidebar.info("Type a filter request above.")

    if st.sidebar.button("Reset Filter (Show All)"):
        st.session_state.filter_query = None
        st.sidebar.info("Filter cleared.")

    filtered_df = df.copy()
    if st.session_state.filter_query:
        try:
            filtered_df = df.query(st.session_state.filter_query)
        except Exception as e:
            st.sidebar.error(f"AI filter failed: {e}. Showing all data.")
            filtered_df = df.copy()

    summary = analysis.get_summary(filtered_df, uploaded_file.name)

    # ==========================
    # SMART DOWNLOAD BUTTON
    # ==========================
    if df.shape[0] == filtered_df.shape[0]:
        st.sidebar.download_button(
            label="📥 Download Full CSV",
            data=filtered_df.to_csv(index=False),
            file_name="full_dataset.csv",
            mime="text/csv"
        )
    else:
        st.sidebar.download_button(
            label=f"📥 Download AI-Filtered CSV ({filtered_df.shape[0]} rows)",
            data=filtered_df.to_csv(index=False),
            file_name="ai_filtered_dataset.csv",
            mime="text/csv"
        )

    # ==========================
    # HOME - AUTO INSIGHTS
    # ==========================
    if option == "Home":
        st.divider()
        if filtered_df.empty:
            st.warning("The current filter returned 0 rows. Cannot generate insights.")
        elif st.button("✨ Auto-Generate Key Insights from Data"):
            with st.spinner("AI is scanning your dataset for hidden trends..."):
                insight_question = "Analyze this dataset and give me exactly 3 key business insights or trends that a data analyst would find interesting. Keep each insight to 1-2 sentences."
                insights = ai_helper.ask_ai(insight_question, summary)
            
            st.subheader("🔑 Key Insights")
            st.markdown(insights)
            
            st.divider()
            if st.button("📄 Export Insights to PDF"):
                pdf_file = analysis.export_to_pdf(insights)
                if pdf_file:
                    with open(pdf_file, "rb") as f:
                        st.download_button(label="Download PDF Report", data=f, file_name="AI_Analysis_Report.pdf", mime="application/pdf")

    # ==========================
    # SUMMARY
    # ==========================
    if option == "Dataset Summary":
        st.header("📊 Dataset Summary")
        c1, c2, c3 = st.columns(3)
        c1.metric("Rows", filtered_df.shape[0])
        c2.metric("Columns", filtered_df.shape[1])
        c3.metric("Missing Values", int(filtered_df.isnull().sum().sum()))
        st.divider()
        st.subheader("Preview")
        st.dataframe(filtered_df.head(10), use_container_width=True)
        st.subheader("Column Names")
        st.write(list(filtered_df.columns))
        st.subheader("Data Types")
        st.dataframe(pd.DataFrame(filtered_df.dtypes, columns=['Data Type']))
        st.subheader("Missing Values")
        st.dataframe(pd.DataFrame(filtered_df.isnull().sum(), columns=['Missing Values']))

    # ==========================
    # STATISTICS
    # ==========================
    if option == "Statistics":
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
            st.write(analysis.get_category_counts(filtered_df, col))

    # ==========================
    # VISUALIZATION
    # ==========================
    if option == "Visualization":
        st.header("📊 Interactive Visualization")
        st.info("💡 Hover over the charts for details! Click the 📷 camera icon on the chart to download as PNG.")
        
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
        elif filtered_df.empty:
            st.warning("No data available to plot based on the current filter.")

        st.divider()
        if st.button("🤖 Explain this Chart with AI"):
            if fig is not None:
                with st.spinner("AI is analyzing the chart..."):
                    chart_question = f"Briefly explain the {chart_type} for the column(s) selected. Provide a simple insight."
                    explanation = ai_helper.ask_ai(chart_question, summary)
                st.success("AI Explanation:")
                st.write(explanation)
            else:
                st.warning("Please generate a chart first.")

    # ==========================
    # ASK AI
    # ==========================
    if option == "Ask AI":
        st.header("🤖 Ask AI")
        question = st.text_input("Ask about your dataset")
        if st.button("Get Answer"):
            if question.strip() == "":
                st.warning("Enter a question")
            else:
                with st.spinner("AI analyzing..."):
                    answer = ai_helper.ask_ai(question, summary)
                st.success("AI Response")
                st.write(answer)

else:
    st.info("Upload a CSV file from sidebar.")
