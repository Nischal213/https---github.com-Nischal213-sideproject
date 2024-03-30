import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Login Page")

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("user_data/data.csv")


def does_username_exist(username):
    if username:
        return any(i == username for i in df["Username"])
    else:
        return ""


def is_password_correct(password, username):
    try:
        get_password = df.loc[df["Username"] == f"{username}", "Password"]
        if password == get_password.values[0]:
            return True
    except (KeyError, IndexError):
        return False


st.image("static/game_logo.png")
username = st.text_input("Username", max_chars=20, placeholder="Enter your username")
user_result = does_username_exist(username)
if user_result == False:
    st.error("Username does not exist")
password = st.text_input("Password", type="password", placeholder="Enter your password")
pass_result = is_password_correct(password, username)
submit_button = st.button("Log In", type="primary")
st.markdown(
    "<div id = 'has_account'><p> Don't have an account? Sign Up <a href='http://localhost:8501/' target='_self'>Here</a></p></div>",
    unsafe_allow_html=True,
)
if submit_button:
    if user_result == True and pass_result == True:
        if "user" not in st.session_state:
            st.session_state["user"] = username
        switch_page("home")
    else:
        st.warning("Not all the fields are valid")
