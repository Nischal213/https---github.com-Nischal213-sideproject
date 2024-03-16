import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Game Page")

# adding bootstrap styling
st.markdown(
    ' <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# top navbar
with open("static/top-nav.html") as f:
    st.markdown(f"{f.read()}", unsafe_allow_html=True)

st.markdown(
    "<div id = 'header'><h1>Welcome to</h1></div>",
    unsafe_allow_html=True,
)
st.image("static/game_logo.png")
st.markdown(
    "<div id = 'sub-header'><h2>Pick a difficulty</h2></div>",
    unsafe_allow_html=True,
)

# game difficulty descriptions
with open("static/difficulty.html") as f:
    st.markdown(f"{f.read()}", unsafe_allow_html=True)

st.markdown('<span id="easy-button"></span>', unsafe_allow_html=True)
easy_mode = st.button("Play!", key="easy")
st.markdown('<span id="medium-button"></span>', unsafe_allow_html=True)
medium_mode = st.button("Play!", key="medium")
st.markdown('<span id="hard-button"></span>', unsafe_allow_html=True)
hard_mode = st.button("Play!", key="hard")

if easy_mode:
    switch_page("easy difficulty")

if medium_mode:
    switch_page("medium difficulty")

if hard_mode:
    switch_page("hard difficulty")
