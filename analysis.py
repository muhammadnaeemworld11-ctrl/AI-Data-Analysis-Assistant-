import pandas as pd
import numpy as np
import streamlit as st
import io

# Reads the CSV file with fallback encodings
@st.cache_data
def load_data(bytes_data):
    """Reads the CSV file with fallback encodings. Cached for speed."""
    try:
        return pd.read_csv(io.BytesIO(bytes_data), encoding='utf-8')
    except UnicodeDecodeError:
        # No need for seek(0) anymore since we create a fresh BytesIO object
        return pd.read_csv(io.BytesIO(bytes_data), encoding='latin1')
    except Exception as e:
        # Catch other parsing errors (e.g., empty file, corrupt CSV)
        st.error(f"Error reading CSV: {e}")
        return None

def get_summary(df, filename):
    """Generates a text summary of the dataset for the AI."""
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
    numeric = df.select_dtypes(include=[np.number]) 
    if not numeric.empty: 
        return numeric.describe()
    return None

def get_category_counts(df, col):
    """Returns value counts for a categorical column."""
    if col in df.columns:
        counts = df[col].value_counts().reset_index()
        counts.columns = [col, 'Count']
        return counts
    return None

def clean_data(df):
    """Cleans the dataset by removing duplicates and null values."""
    df = df.copy() 
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df
