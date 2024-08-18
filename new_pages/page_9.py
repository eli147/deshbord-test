import streamlit as st
import pandas as pd
import yfinance as yf
from mongo import insert_user_name, find_user_name,delete_user


def get_all_data(user_name: str):
    """Fetch data for a given username from the database."""
    data = find_user_name(user_name)
    return data


def run():
    st.title('User Management System')

    # Input for creating a new user
    user_name = st.text_input('Enter user name:')
    amount = 100000  # Default amount to associate with a new user

    # Check if the user already exists
    if user_name:
        existing_user = get_all_data(user_name)
        print(existing_user)
        if existing_user:
            st.error('User name already exists.')
            user_delete = st.button('Delete a user_name ')
            if user_delete:
                delete_user(user_name)
        elif st.button('Create User'):
            # Save new user if not already in the database
            insert_user_name(user_name, amount)
            st.success(f"User '{user_name}' saved successfully.")
    else:
        if st.button('Save User'):
            st.error("Please enter a user name.")
