import streamlit as st
import os


def does_username_exist(username):
    return bool(
        [i for i in os.listdir("user_data") if i.removesuffix(".txt") == username]
    )


def is_password_correct(password, username):
    if does_username_exist(username):
        with open(f"user_data/{username}.txt") as f:
            content = f.readlines()[1][10:]
            if password == content.strip():
                return True
    else:
        return False


st.write("Hello another world")
username = st.text_input("Username", max_chars=20)
if len(username) == 0:
    st.info("Enter your username")
    user_result = False
else:
    user_result = does_username_exist(username)
    if user_result == False:
        st.error("Username does not exist")
password = st.text_input("Password", type="password")
if len(password) == 0:
    st.info(f"Enter a secure password")
    pass_result = False
else:
    pass_result = is_password_correct(password, username)
    print(pass_result)
    if pass_result == False:
        st.error("Invalid password")
