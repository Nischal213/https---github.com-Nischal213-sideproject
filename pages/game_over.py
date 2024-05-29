import streamlit as st
import plotly.express as px
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Math Maestro | Game Over")
# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "user" not in st.session_state:
    switch_page("error page")

st.markdown(
    """
    <div id='game-over-header'>
        <h1>GAME OVER</h1>
    </div>""",
    unsafe_allow_html=True,
)
df = {
    "Answers": ["Incorrect", "Correct"],
    "Points": [
        st.session_state["asked_questions"] - st.session_state["stored_points"],
        st.session_state["stored_points"],
    ],
}
figure = px.pie(
    data_frame=df,
    names="Answers",
    values="Points",
    color_discrete_sequence=["Red", "Green"],
    title="Game overview",
)
st.plotly_chart(figure)
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
st.markdown("<span id='retry-btn'></span>", unsafe_allow_html=True)
retry = st.button("Retry")
if retry:
    switch_page("home")
