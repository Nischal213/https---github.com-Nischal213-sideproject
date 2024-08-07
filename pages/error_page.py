import streamlit as st

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write(
    "<h1>401 Error , You must be logged in </h1>",
    unsafe_allow_html=True,
)

st.write(
    "<div id = 'header_error'><h4>Click <a href='http://localhost:8501/login_page' target='_self'> here </a> to be redirected to the main page </h4></div>",
    unsafe_allow_html=True,
)
