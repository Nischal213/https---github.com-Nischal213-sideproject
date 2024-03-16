import streamlit as st
import random
from streamlit_extras.switch_page_button import switch_page
import time


# function to check if a variable is a type of the parameter
def is_type(variable, type):
    try:
        variable = type(variable)
        return True
    except ValueError:
        return False


# function to generate random numbers
def generate_random_question():
    random_op = random.choice(["+", "-", "*", "/"])
    if random_op in ["/", "*"]:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    else:
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
    answer = round(eval(f"{num1} {random_op} {num2}"), 1)
    if random_op == "/":
        return f"What is {num1} {random_op} {num2}? (To 1 d.p)", answer
    else:
        return f"What is {num1} {random_op} {num2}?", answer


# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

"""
IMPORTANT , as of now , if the user dies then goes back to the same difficulty, the lives will remain the same
to fix this clear the session keys. But before this, make sure to title this problem as problem4
"""

st.markdown(
    "<div id = 'sub-header'><h2><span style='color:green;'>Easy Difficulty</h2></span></div>",
    unsafe_allow_html=True,
)
# storing user data and questions in the session
if "easy_question" not in st.session_state:
    st.session_state["easy_question"], st.session_state["easy_ans"] = (
        generate_random_question()
    )
    st.session_state["easy_points"], st.session_state["easy_lives"] = 0, 5
st.markdown('<span id="question"></span>', unsafe_allow_html=True)
question_box = st.empty()
question_box.write(
    f"<p>{st.session_state['easy_question']}</p>", unsafe_allow_html=True
)
padding_left, input, padding_right = st.columns([1, 3, 1])
user_ans = input.text_input(
    " ", help="Get as many answers correct as possible before you run out of lives"
)
info_box = st.empty()
info_box.write(
    f"<div id = 'info'><h3>Points : {st.session_state['easy_points']}</h3><h3>Lives : {st.session_state['easy_lives']}</h3></div>",
    unsafe_allow_html=True,
)
st.markdown('<span id="check-button"></span>', unsafe_allow_html=True)
button = st.button("Check")
st.markdown('<span id="info-message"></span>', unsafe_allow_html=True)
padding_left, invalid_format, padding_right = st.columns([1, 3, 1])
st.markdown('<span id="error-message"></span>', unsafe_allow_html=True)
padding_left, incorrect_answer, padding_right = st.columns([1, 3, 1])
if button:
    # checks if the user input is an int or float
    if is_type(user_ans, int) or is_type(user_ans, float):
        st.markdown(
            "<style>.element-container:has(#check-button) + div button{display:none;}</style>",
            unsafe_allow_html=True,
        )
        # checks if the user's answer is correct
        if round(float(user_ans), 1) == round(float(st.session_state["easy_ans"]), 1):
            st.session_state["easy_points"] += 1
            info_box.write(
                f"<div id = 'info'><h3 style='color:green;'>+1</h3><h3>Lives : {st.session_state['easy_lives']}</h3></div>",
                unsafe_allow_html=True,
            )
            time.sleep(1)
            info_box.write(
                f"<div id = 'info'><h3>Points : {st.session_state['easy_points']}</h3><h3>Lives : {st.session_state['easy_lives']}</h3></div>",
                unsafe_allow_html=True,
            )
        else:
            incorrect_answer.error(
                f"Incorrect! The answer was {st.session_state['easy_ans']}"
            )
            st.session_state["easy_lives"] -= 1
            if st.session_state["easy_lives"] == 0:
                switch_page("game page")
            info_box.write(
                f"<div id = 'info'><h3>Points : {st.session_state['easy_points']}</h3><h3 style='color:red;'>-1</h3></div>",
                unsafe_allow_html=True,
            )
            time.sleep(1)
            info_box.write(
                f"<div id = 'info'><h3>Points : {st.session_state['easy_points']}</h3><h3>Lives : {st.session_state['easy_lives']}</h3></div>",
                unsafe_allow_html=True,
            )
        st.markdown(
            "<style>.element-container:has(#check-button) + div button{display:flex;}</style>",
            unsafe_allow_html=True,
        )
        # generates a new random question
        st.session_state["easy_question"], st.session_state["easy_ans"] = (
            generate_random_question()
        )
        # updating the box to display the newly generated question
        question_box.write(
            f"<p>{st.session_state['easy_question']}</p>", unsafe_allow_html=True
        )
        # rerunning the script for the visual effects
        st.rerun()

    # else, an error message is flagged
    else:
        invalid_format.info("Invalid format")
