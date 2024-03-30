
import pandas as pd
import streamlit 


def upload_csv():
    uploaded_file = streamlit.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None