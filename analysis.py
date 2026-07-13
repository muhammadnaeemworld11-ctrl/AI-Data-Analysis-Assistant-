import pandas as pd
from fpdf import FPDF
import tempfile

def load_data(file):
    """
    Safely reads CSV datasets by checking standard encoding parameters
    to prevent UnicodeDecodeErrors with windows-based or localized files.
    """
    try:
        # Step 1: Try reading with standard UTF-8 encoding
        return pd.read_csv(file)
    except UnicodeDecodeError:
        try:
            # Step 2: Seek back to the beginning of the file stream before trying again
            file.seek(0)
            # Try reading with ISO-8859-1 (Latin-1) which is common for retail data
            return pd.read_csv(file, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            # Step 3: Seek back to the beginning of the file stream one last time
            file.seek(0)
            # Try reading with Windows-1252 encoding (standard Excel export fallback)
            return pd.read_csv(file, encoding='cp1252')

def clean_data(df):
    # Strip whitespaces from string columns to prevent trailing lookup errors
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()
    return df

def get_summary(df, filename):
    """
    Generates a textual breakdown of the dataset. 
    All data type references are safely cast to strings to protect PyArrow.
    """
    total_rows = df.shape[0]
    total_cols = df.shape[1]
    
    # Secure mapping of column data types
    dtypes_dict = {col: str(dtype) for col, dtype in df.dtypes.items()}
    missing_values = df.isnull().sum().to_dict()
    
    summary_text = f"Dataset Name: {filename}\n"
    summary_text += f"Total Rows: {total_rows}, Total Columns: {total_cols}\n\n"
    summary_text += "Columns, Data Types, and Missing Values Breakdown:\n"
    
    for col in df.columns:
        summary_text += f"- Column: '{col}' | Type: {dtypes_dict[col]} | Missing: {missing_values[col]}\n"
        
    return summary_text

def get_numeric_stats(df):
    numeric_df = df.select_dtypes(include='number')
    if numeric_df.empty:
        return None
    return numeric_df.describe().T

def get_category_counts(df, column):
    return df[column].value_counts().head(10)

def export_to_pdf(text_content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Process long string lines safely for FPDF output
    for line in text_content.split('\n'):
        # Clean potential non-latin characters that break standard FPDF layout engines
        clean_line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(200, 10, txt=clean_line, ln=True)
        
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf.output(tmp.name)
        return tmp.name
