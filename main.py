import streamlit as st
import hmac
from services.launch_lr import launch_linear_regression
from services.select_param import select_parameters
from services.upload_csv import select_columns, upload_csv


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

else:
    st.title("Linear Regression Model")
    
    df = upload_csv()
    if df is None:
        st.warning("Please upload a CSV file.")
    else:
        st.write("### Data Preview")
        st.write(df.head())
        
        # Select X and y columns
        X_columns, y_column = select_columns(df)
        
        st.write("### Selected Columns")
        st.write("X (features):", X_columns)
        st.write("y (target variable):", y_column)
        
    
        fit_intercept, copy_X, n_jobs, positive = select_parameters()

        print(X_columns)
        print(y_column)
        
        if st.button("Launch Linear Regression Model"):
            mean_mae, test_mae = launch_linear_regression(df, X_columns, y_column, fit_intercept, copy_X, n_jobs, positive)
            st.write("Mean Absolute Error (5-fold CV): {:.2f}%".format(mean_mae))
            st.write("Mean Absolute Error (Test set): {:.2f}%".format(test_mae))


