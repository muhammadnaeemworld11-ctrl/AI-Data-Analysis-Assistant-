# AI Data Analysis Assistant 🤖

A simple AI-powered Data Analysis Assistant built with Python, Streamlit, and the OpenRouter API. This application allows users to upload datasets, automatically generate statistical evaluations, render dynamic visual charts, and query an LLM directly regarding the structural insights of their data.

---

## 🚀 Features

* **✅ Dataset Operations**: Seamlessly upload and preview custom CSV datasets.
* **✅ Automatic Statistics**: Instant calculations for numeric ranges (Mean, Max, Min, Counts).
* **✅ Rich Data Visualization**: Generate interactive charts (Bar, Histogram, Pie, Scatter) with automated titles and clean labels.
* **✅ AI Key Insights**: Automated generation of 3 succinct business trends from structural meta-data.
* **✅ Natural Language Interface**: Ask descriptive questions about your data layout or attributes directly to an integrated AI assistant.

---

## 🛠️ Setup Instructions

### 1. Clone or Download the Repository
Ensure all project files (`main.py`, `analysis.py`, `visualization.py`, `ai_helper.py`) are placed in the same working directory.

### 2. Install Dependencies
Run the following pip command in your terminal to install the necessary framework packages:
```bash
pip install -r requirements.txt
```

### 3. Configure API Credentials
Create a file named `.env` in the root of your project directory and add your OpenRouter developer credential:
```env
OPENROUTER_API_KEY=your_key_here
```

### 4. Execute the Application
Launch the local Streamlit web server instance using:
```bash
streamlit run main.py
```

---

## 📁 Project Structure

* **`main.py`** – Core application architecture layout, UI configuration, sidebar navigation, and session execution logic.
* **`analysis.py`** – Internal processing module for handling dataframe loading, text cleaning, text summaries, and structural matrix statistics.
* **`visualization.py`** – Configuration module utilizing Plotly Express pipelines to render responsive data graphs.
* **`ai_helper.py`** – Upstream connection management handling system context prompt parsing and inference streaming via OpenRouter API clients.
* **`dataset.csv`** – Sample evaluation file containing standard formatting datasets (e.g., IMDB movies dataset).
* **`requirements.txt`** – System application dependencies declarations file.
* **`README.md`** – Clear engineering execution layout documentation.
