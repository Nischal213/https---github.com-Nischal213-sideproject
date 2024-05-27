import streamlit as st
import pandas as pd
import time
import datetime
from AdaptiveQuestions import AdaptiveQuestions
from streamlit_extras.switch_page_button import switch_page


# function to check if a variable is a type of the parameter
def is_type(variable, type):
    try:
        variable = type(variable)
        return True
    except ValueError:
        return False


# function that shows the visual effects of "+1" or "-1"
# temporarily for lives/points
def animation(before_animation, after_animation, box_name, duration=1):
    box_name.write(f"{before_animation}", unsafe_allow_html=True)
    time.sleep(duration)
    box_name.write(f"{after_animation}", unsafe_allow_html=True)


# function to generate random questions
def generate_random_question(avg_score, arr=[], diff=None):
    instance = AdaptiveQuestions(avg_score, arr, diff)
    question, answer, one_dp, diff = instance.generate_initial_question()
    return question, answer, one_dp, diff


if "user" not in st.session_state:
    switch_page("error page")

if "playing" in st.session_state and not (st.session_state["playing"]):
    for key in st.session_state.keys():
        if key != "user":
            del st.session_state[key]

if "question" not in st.session_state:
    df = pd.read_csv(f"user_data/{st.session_state['user']}.csv")
    avg_score = sum(df["Points"]) / len(df["Points"])
    question, answer, one_dp, diff = generate_random_question(avg_score)
    st.session_state["question"], st.session_state["ans"] = question, answer
    st.session_state["one_dp"], st.session_state["stored_points"] = one_dp, 0
    st.session_state["points"], st.session_state["lives"] = 0, 7
    st.session_state["array"], st.session_state["asked_questions"] = [], 0
    st.session_state["difficulty"] = diff

st.set_page_config(page_title="Math Maestro | Adaptive Mode")

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("main_data/data.csv")
st.markdown(
    """
    <div id = 'sub-header'>
        <h2>
            <span style='color:blue;'>
            Adaptive Difficulty
            </span>
        </h2>
    </div>""",
    unsafe_allow_html=True,
)
# name of all the keys added in the session
keys = ["question", "ans", "one_dp", "points", "lives", "array"]
st.markdown('<span id="question"></span>', unsafe_allow_html=True)
question_box = st.empty()
if st.session_state["difficulty"] != "Hard":
    question_box.write(f"<p>{st.session_state['question']}</p>", unsafe_allow_html=True)
else:
    question_box.latex(f"{st.session_state['question']}")
padding_left, input, padding_right = st.columns([1, 3, 1])
if st.session_state["difficulty"] == "Easy":
    input_msg = "Find the answer"
if st.session_state["difficulty"] == "Medium" and st.session_state["one_dp"]:
    input_msg = "Find y to 1 d.p"
elif st.session_state["difficulty"] == "Medium":
    input_msg = "Find y"
if st.session_state["difficulty"] == "Hard" and st.session_state["one_dp"]:
    input_msg = "Find x to 1.dp"
elif st.session_state["difficulty"] == "Hard":
    input_msg = "Find x"
user_ans = input.text_input(
    f"{input_msg}",
    help="Get as many answers correct as possible before you run out of lives",
)
info_box = st.empty()
info_box.write(
    f"""
    <div id = 'info'>
        <h3>Points : {st.session_state['points']}</h3>
        <h3>Lives : {st.session_state['lives']}</h3>
    </div>""",
    unsafe_allow_html=True,
)
st.markdown('<span id="check-button"></span>', unsafe_allow_html=True)
button = st.button("Check")
st.markdown('<span id="info-message"></span>', unsafe_allow_html=True)
padding_left, invalid_format, padding_right = st.columns([1, 3, 1])
st.markdown('<span id="error-message"></span>', unsafe_allow_html=True)
padding_left, incorrect_answer, padding_right = st.columns([1, 3, 1])
if button:
    if is_type(user_ans, int) or is_type(user_ans, float):
        st.markdown(
            """
            <style>
            .element-container:has(#check-button) + div button{
                display:none;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        # checks if the user's answer is correct
        if round(float(user_ans), 1) == round(float(st.session_state["ans"]), 1):
            st.session_state["array"].append(1)
            st.session_state["asked_questions"] += 1
            st.session_state["points"] += 1
            before_msg = f"""
            <div id = 'info'>
                <h3 style='color:green;'>+1</h3>
                <h3>Lives : {st.session_state['lives']}</h3>
            </div>"""
            after_msg = f"""
            <div id = 'info'>
                <h3>Points : {st.session_state['points']}</h3>
                <h3>Lives : {st.session_state['lives']}</h3>
            </div>"""
            animation(before_msg, after_msg, info_box)
        else:
            incorrect_answer.error(
                f"Incorrect! The answer was {st.session_state['ans']}"
            )
            st.session_state["array"].append(0)
            st.session_state["asked_questions"] += 1
            st.session_state["lives"] -= 1
            if st.session_state["lives"] == 0:
                st.session_state["difficulty"] = "Adaptive"
                # Adds the point to their personal record along with current
                # date and time
                with open(f"user_data/{st.session_state['user']}.csv", "a") as f:
                    current_time = datetime.datetime.now()
                    format_time = current_time.strftime("%d/%m/%y")
                    f.write("\n")
                    f.write(f"{st.session_state['points']},{format_time}")
                for key in keys:
                    # deletes all the added session keys
                    del st.session_state[key]
                switch_page("game over")
            before_msg = f"""
            <div id='info'>
                <h3>Points : {st.session_state['points']}</h3>
                <h3 style='color:red;'>-1</h3>
            </div>"""
            after_msg = f"""
            <div id = 'info'>
                <h3>Points : {st.session_state['points']}</h3>
                <h3>Lives : {st.session_state['lives']}</h3>
            </div>"""
            animation(before_msg, after_msg, info_box)
        st.markdown(
            """
            <style>
            .element-container:has(#check-button) + div button{
                display:flex;
            }
            </style>""",
            unsafe_allow_html=True,
        )
        # generates a new random question
        if len(st.session_state["array"]) == 5:
            question, answer, one_dp, diff = generate_random_question(
                -1, st.session_state["array"], None
            )
            st.session_state["question"] = question
            st.session_state["ans"] = answer
            st.session_state["one_dp"] = one_dp
            st.session_state["difficulty"] = diff
            st.session_state["array"] = []
        else:
            question, answer, one_dp, diff = generate_random_question(
                -1, st.session_state["array"], st.session_state["difficulty"]
            )
            st.session_state["question"] = question
            st.session_state["ans"] = answer
            st.session_state["one_dp"] = one_dp
        # updating the box to display the newly generated question
        if st.session_state["difficulty"] != "Hard":
            question_box.write(
                f"<p>{st.session_state['question']}</p>", unsafe_allow_html=True
            )
        else:
            question_box.latex(f"{st.session_state['question']}")
        # rerunning the script for the visual effects
        st.rerun()

    # else, an error message is flagged
    else:
        invalid_format.info("Invalid format")
