import streamlit as st
import os

with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def does_username_exist(username):
    if username:
        return bool(
            [i for i in os.listdir("user_data") if i.removesuffix(".txt") == username]
        )
    else:
        return ""


def is_password_correct(password, username):
    if username:
        if does_username_exist(username):
            with open(f"user_data/{username}.txt") as f:
                content = f.readlines()[1][10:]
                if password == content.strip():
                    return True
        else:
            return False
    else:
        return ""


st.write("Hello another world")
username = st.text_input("Username", max_chars=20)
user_result = does_username_exist(username)
if user_result == False:
    st.error("Username does not exist")
password = st.text_input("Password", type="password")
if user_result:
    pass_result = is_password_correct(password, username)
    if pass_result == False:
        st.error("Invalid password")
submit_button = st.button("Log In", type="secondary")
if submit_button:
    if user_result == True and pass_result == True:
        st.success("Logged In")
    else:
        st.warning("Not all the fields are valid")
