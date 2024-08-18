import streamlit as st
from mongo import get_all_users


def run():
    st.title('Get all Users !')
    data = get_all_users()
    st.table(data)
