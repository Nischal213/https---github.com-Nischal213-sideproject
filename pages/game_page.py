import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Game Page")

with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
