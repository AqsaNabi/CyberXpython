import streamlit as st
import json


def load_data():
    with open("passs.json", "r") as f:
        data = json.load(f)
    return data


data = load_data()


def authenticate_user(user, passwd):
    for key in data:
        if data[key]["name"] == user and data[key]["password"] == passwd:
            return True

    return False


user = st.text_input("Username:")
passwd = st.text_input("Password:", type="password")

if st.button("Login"):

    if authenticate_user(user, passwd):

        st.success("Login successful!")

        # Form shown after successful login
        st.subheader("Student Form")

        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=100)
        email = st.text_input("Email")

        if st.button("Submit Form"):
            st.success("Form submitted successfully!")

    else:
        st.error("Invalid ID or Password")

