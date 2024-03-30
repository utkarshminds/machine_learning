import streamlit as st

def select_parameters():
    fit_intercept = st.checkbox("Fit Intercept")
    copy_X = st.checkbox("Copy X")
    n_jobs = st.number_input("Number of Jobs", min_value=1, value=1)
    positive = st.checkbox("Positive")
    return fit_intercept, copy_X, n_jobs, positive