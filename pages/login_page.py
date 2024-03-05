import streamlit as st
import os


def does_username_exist(username):
    return bool(
        [i for i in os.listdir("user_data") if i.removesuffix(".txt") == username]
    )


st.write("Hello another world")
username = st.text_input("Username", max_chars=20)
if len(username) == 0:
    st.info("Enter your username")
else:
    user_result = does_username_exist(username)
    if user_result == False:
        st.error("Username does not exist")
