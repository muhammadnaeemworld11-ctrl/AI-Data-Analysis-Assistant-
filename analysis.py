import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data(uploaded_file):
    try:
        return pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        uploaded_file.seek(0)
        return pd.read_csv(uploaded_file, encoding='latin1')

def get_summary(df, filename):
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
    numeric = df.select_dtypes(include=[np.number]) 
    if not numeric.empty: 
        return numeric.describe()
    return None

def get_category_counts(df, col):
    if col in df.columns:
        counts = df[col].value_counts().reset_index()
        counts.columns = [col, 'Count']
        return counts
    return None

def clean_data(df):
    df = df.copy() 
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df
