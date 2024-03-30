import streamlit as st
import pandas as pd

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write(
    "<h1>401 Error , You must be logged in </h1>",
    unsafe_allow_html=True,
)

st.write(
    "<div id = 'header_error'><h4>Click <a href='http://localhost:8501/' target='_self'> here </a> to be redirected to the main page </h4></div>",
    unsafe_allow_html=True,
)
df = pd.read_csv("user_data/data.csv")
extracted_df = df[["Username", "Easy_points"]].sort_values(
    by="Easy_points", ascending=False
)
top_3 = extracted_df[:3]
for i, j in zip(top_3["Username"], top_3["Easy_points"]):
    print(i, j)
