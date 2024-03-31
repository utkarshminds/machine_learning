
import pandas as pd
import streamlit as st


def upload_csv():
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None

def select_columns(df):
    st.write("### Select Columns for X and y")
    
    # Selecting columns for X
    st.write("#### Select columns for X (features)")
    selected_X_columns = st.multiselect("Select columns for X", df.columns.tolist())

    # Selecting column for y
    st.write("#### Select column for y (target variable)")
    selected_y_column = st.selectbox("Select column for y", df.columns.tolist())

    return selected_X_columns, selected_y_column