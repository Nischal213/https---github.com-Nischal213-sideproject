import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Game Over")
# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# adding bootstrap styling for top navbar
st.markdown(
    ' <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

# top navbar
with open("pages/top-nav.html") as f:
    st.markdown(f"{f.read()}", unsafe_allow_html=True)

df = pd.read_csv("user_data/data.csv")

if "user" not in st.session_state:
    switch_page("error page")

st.markdown(
    """
    <div id='game-over-header'>
        <h1>GAME OVER</h1>
    </div>""",
    unsafe_allow_html=True,
)
labels = ["Correct Answers", "Incorrect Answers"]
array = [
    st.session_state["stored_points"],
    (st.session_state["asked_questions"] - st.session_state["stored_points"]),
]
colors = ["#2ecc71", "#e74c3c"]
fig, ax = plt.subplots()
# Matching background color with streamlit's dark mode
fig.set_facecolor("#0e1117")
_, texts, _ = ax.pie(
    x=array,
    shadow=True,
    autopct="%1.1f%%",
    explode=(0.1, 0),
    labels=labels,
    colors=colors,
)

# Setting the text color in the pie chart to white
for text in texts:
    text.set_color("white")

st.markdown('<span id="user-stats"></span>', unsafe_allow_html=True)
st.pyplot(fig)
st.write(
    f"""
    <div id = 'game-stats'>
        <h3>
            You scored {st.session_state['stored_points']} points
            in {st.session_state['difficulty']} difficulty
        </h3>
    </div>""",
    unsafe_allow_html=True,
)
