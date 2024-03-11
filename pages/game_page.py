import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Game Page")
# adding bootstrap styling
st.markdown(
    ' <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
# web styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# top navbar
with open("static/top-nav.html") as f:
    st.markdown(f"{f.read()}", unsafe_allow_html=True)
# header
st.markdown(
    "<div id = 'header'><h1>Welcome to</h1></div>",
    unsafe_allow_html=True,
)
st.image("static/game_logo.png")
