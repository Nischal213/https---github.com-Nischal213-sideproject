import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Login Page")

with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def does_username_exist(username):
    if username:
        return any(i.removesuffix(".txt") == username for i in os.listdir("user_data"))
    else:
        return ""


def is_password_correct(password, username):
    if does_username_exist(username):
        with open(f"user_data/{username}.txt") as f:
            content = f.readlines()[1][10:]
            if password == content.strip():
                return True
    else:
        return False


st.image("static/game_logo.png")
username = st.text_input("Username", max_chars=20, placeholder="Enter your username")
user_result = does_username_exist(username)
if user_result == False:
    st.error("Username does not exist")
password = st.text_input("Password", type="password", placeholder="Enter your password")
pass_result = is_password_correct(password, username)
submit_button = st.button("Log In", type="secondary")
st.markdown(
    "<div id = 'has_account'><p> Don't have an account? Sign Up <a href='http://localhost:8501/' target='_self'>Here</a></p></div>",
    unsafe_allow_html=True,
)
if submit_button:
    if user_result == True and pass_result == True:
        switch_page("game page")
    else:
        st.warning("Not all the fields are valid")
