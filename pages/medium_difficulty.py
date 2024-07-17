import streamlit as st
import pandas as pd
import time
import random
import datetime
from streamlit_extras.switch_page_button import switch_page
from EquationSolver import EquationSolver


# function to check if a variable is a type of the parameter
def is_type(variable, type):
    try:
        variable = type(variable)
        return True
    except ValueError:
        return False


def generate_random_values():
    dict = {"+": "-", "-": "+", "*": "/", "/": "*"}
    random_op, random_op2 = random.choice(list(dict.keys())), random.choice(
        list(dict.keys())
    )
    num1, num2, num3 = (
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10),
    )
    # In the class , the reverse of the first operator is not needed anywhere
    reverse_op2 = dict.get(random_op2)
    return num1, num2, num3, random_op, random_op2, reverse_op2


def generate_random_question():
    num1, num2, num3, random_op, random_op2, reverse_op2 = generate_random_values()
    instance = EquationSolver(num1, num2, num3, random_op, random_op2, reverse_op2)
    question = instance.get_question()
    answer, one_dp = instance.get_answer()
    # In the class , None is returned if there is a ZeroDivisionError
    while answer is None:
        num1, num2, num3, random_op, random_op2, reverse_op2 = generate_random_values()
        instance = EquationSolver(num1, num2, num3, random_op, random_op2, reverse_op2)
        question = instance.get_question()
        answer, one_dp = instance.get_answer()
    return question, answer, one_dp


# function that shows the visual effects of "+1" or "-1"
# temporarily for lives/points
def animation(before_animation, after_animation, box_name, duration=1):
    box_name.write(f"{before_animation}", unsafe_allow_html=True)
    time.sleep(duration)
    box_name.write(f"{after_animation}", unsafe_allow_html=True)


if "user" not in st.session_state:
    switch_page("error page")


# This block of code is used to ensure that if the user attempts
# to go back to the home page whilst in a game, it will handle
# things accordingly
if "playing" in st.session_state and not (st.session_state["playing"]):
    for key in st.session_state.keys():
        if key != "user":
            del st.session_state[key]

st.set_page_config(page_title="Math Maestro | Medium Mode")


# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("main_data/data.csv")
st.markdown(
    """
    <div id = 'sub-header'>
        <h2>
            <span style='color:#FF6347;'>
            Medium Difficulty
            </span>
        </h2>
    </div>""",
    unsafe_allow_html=True,
)
# name of all the keys added in the session
keys = ["question", "ans", "one_dp", "points", "lives"]

# storing user data and questions in the session
if "question" not in st.session_state:
    question, answer, one_dp = generate_random_question()
    st.session_state["question"], st.session_state["ans"] = question, answer
    st.session_state["one_dp"], st.session_state["stored_points"] = one_dp, 0
    st.session_state["points"], st.session_state["lives"] = 0, 4
    st.session_state["difficulty"], st.session_state["asked_questions"] = "Medium", 0

st.markdown('<span id="question"></span>', unsafe_allow_html=True)
question_box = st.empty()
question_box.write(f"<p>{st.session_state['question']}</p>", unsafe_allow_html=True)
padding_left, input, padding_right = st.columns([1, 3, 1])
if st.session_state["one_dp"]:
    input_msg = "Find y to 1.dp"
else:
    input_msg = "Find y"
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
            st.session_state["asked_questions"] += 1
            st.session_state["lives"] -= 1
            if st.session_state["lives"] == 0:
                get_points = df.loc[
                    df["Username"] == st.session_state["user"], "Medium_points"
                ]
                for i in get_points:
                    if i > st.session_state["points"]:
                        change_score = False
                    else:
                        change_score = True

                if change_score:
                    # updates the user's Medium_points score
                    df.loc[
                        df["Username"] == st.session_state["user"], "Medium_points"
                    ] = st.session_state["points"]
                    df.to_csv("main_data/data.csv", index=False)
                st.session_state["stored_points"] = st.session_state["points"]
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
        question, answer, one_dp = generate_random_question()
        st.session_state["question"] = question
        st.session_state["ans"] = answer
        st.session_state["one_dp"] = one_dp
        # updating the box to display the newly generated question
        question_box.write(
            f"<p>{st.session_state['question']}</p>", unsafe_allow_html=True
        )
        # rerunning the script for the visual effects
        st.rerun()

    # else, an error message is flagged
    else:
        invalid_format.info("Invalid format")
