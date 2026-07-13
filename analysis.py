import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data(uploaded_file):
    """Reads the CSV file with fallback encodings. Cached for speed."""
    try:
        return pd.read_csv(uploaded_file, encoding="utf-8")
    except (UnicodeDecodeError, TypeError):
        try:
            return pd.read_csv(uploaded_file, encoding="cp1252")
        except Exception:
            # Added a proper fallback for any other encoding issues
            return pd.read_csv(uploaded_file, encoding="latin1")


def get_summary(df, filename):
    """Generates a text summary of the dataset for the AI."""
    # Using include='all' ensures it works even if there are no numeric columns
    stats = df.describe(include='all').to_string()
    
    return f"""
File: {filename}
Rows: {df.shape[0]}
Columns: {df.shape[1]}
Column Names: {list(df.columns)}
Data Types: {df.dtypes.to_string()}
First Rows: {df.head(5).to_string()}
Statistics: {stats}
"""

def get_numeric_stats(df):
    """Returns statistics for numeric columns."""
    numeric = df.select_dtypes(include=[np.number]) # Fixed format to list
    if not numeric.empty: # More robust check than len(columns)
        return numeric.describe()
    return None

def get_category_counts(df, col):
    """Returns value counts for a categorical column."""
    if col in df.columns:
        return df[col].value_counts()
    return None

def clean_data(df):
    """Cleans the dataset by removing duplicates and null values."""
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df
