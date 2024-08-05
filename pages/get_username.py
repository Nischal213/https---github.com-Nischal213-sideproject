import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Get Username Page")

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "user" in st.session_state:
    switch_page("error page")


def does_username_exist(username):
    if username:
        return any(i == username for i in df["Username"])
    else:
        return ""


st.header("Enter your username")
df = pd.read_csv("main_data/data.csv")
username = st.text_input(
    "Username", max_chars=20, placeholder="Enter a unique username"
)
submit = st.button("Submit", type="primary")
if submit:
    if does_username_exist(username):
        st.session_state["temp_user"] = username
        switch_page("forgot page")
    else:
        st.error("Username does not exist")
