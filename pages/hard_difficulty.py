import random
import streamlit as st
import pandas as pd
import time
import datetime
from streamlit_extras.switch_page_button import switch_page


# function to check if a variable is a type of the parameter
# Has been modified to accept negative values
def is_type(variable, type):
    if str(variable).count("-") == 1:
        variable = variable[1:]
    try:
        variable = type(variable)
        return True
    except ValueError:
        return False


def integrate():
    upper_interval, lower_interval, bigger_power, lower_power = (
        random.randint(1, 10),
        -random.randint(1, 10),
        random.randint(5, 7),
        random.randint(2, 4),
    )
    latex_equation = r"\int_{lower}^{upper} (x^{pow1} + x^{pow2}) dx"
    equation = (
        latex_equation.replace("lower", f"{lower_interval}")
        .replace("upper", f"{upper_interval}")
        .replace("pow1", f"{bigger_power}")
        .replace("pow2", f"{lower_power}")
    )
    bigger_power += 1
    lower_power += 1
    upper_antiderivative = (upper_interval**bigger_power) / bigger_power + (
        upper_interval**lower_power
    ) / lower_power
    lower_antiderivative = (lower_interval**bigger_power) / bigger_power + (
        lower_interval**lower_power
    ) / lower_power
    answer = upper_antiderivative - lower_antiderivative
    if str(answer).count("-"):
        answer = -answer
    return equation, round(answer, 1)


def differentiate():
    value_x, bigger_power, lower_power = (
        random.randint(1, 10),
        random.randint(5, 7),
        random.randint(2, 4),
    )
    latex_equation = r"\frac {dy}{dx} \, (x^{pow1} + x^{pow2}) \, \vert_{\,x={val}}"
    equation = (
        latex_equation.replace("pow1", f"{bigger_power}")
        .replace("pow2", f"{lower_power}")
        .replace("val", f"{value_x}")
    )
    upper_derivative = bigger_power * (value_x) ** (bigger_power - 1)
    lower_derivative = lower_power * (value_x) ** (lower_power - 1)
    answer = upper_derivative + lower_derivative
    return equation, round(answer, 1)


def logarithmics():
    base, exponent = random.randint(2, 5), random.randint(0, 5)
    latex_equation = r"\log_base (x) = exponent"
    equation = latex_equation.replace("base", f"{base}").replace(
        "exponent", f"{exponent}"
    )

    answer = base**exponent
    return equation, round(answer, 1)


def powers():
    base, result = random.randint(2, 10), round(random.uniform(1, 10), 1)
    latex_equation = r"base^x = ans"
    equation = latex_equation.replace("base", f"{base}").replace("ans", f"{result}")

    def natural_log_approximation(number):
        # Reference:
        # https://mathcentral.uregina.ca/QQ/database/QQ.09.02/amanda3.html

        for i in range(10):
            number = number**0.5

        return (number - 1) * 1024

    log_result = natural_log_approximation(result)
    log_base = natural_log_approximation(base)
    answer = log_result / log_base

    return equation, round(answer, 1)


# function that shows the visual effects of "+1" or "-1"
# temporarily for lives/points
def animation(before_animation, after_animation, box_name, duration=1):
    box_name.write(f"{before_animation}", unsafe_allow_html=True)
    time.sleep(duration)
    box_name.write(f"{after_animation}", unsafe_allow_html=True)


if "user" not in st.session_state:
    switch_page("error page")

st.set_page_config(page_title="Math Maestro | Hard Mode")

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("user_data/data.csv")
st.markdown(
    """
    <div id = 'sub-header'>
        <h2>
            <span style='color:red;'>
            Hard Difficulty
            </span>
        </h2>
    </div>""",
    unsafe_allow_html=True,
)
# name of all the keys added in the session
keys = ["question", "ans", "points", "lives"]

func_dict = {
    "integrate": integrate(),
    "differentiate": differentiate(),
    "logs": logarithmics(),
    "powers": powers(),
}

# storing user data and questions in the session
if "question" not in st.session_state:
    random_key = random.choice(list(func_dict.keys()))
    equation, answer = func_dict.get(random_key)
    st.session_state["question"], st.session_state["ans"] = equation, answer
    st.session_state["points"], st.session_state["lives"] = 0, 3
    st.session_state["difficulty"], st.session_state["asked_questions"] = "Hard", 0
    st.session_state["stored_points"] = 0

question_box = st.empty()
question_box.latex(f"{st.session_state['question']}")
padding_left, input, padding_right = st.columns([1, 3, 1])
user_ans = input.text_input(
    f"Find x to 1.dp",
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
                    df["Username"] == st.session_state["user"], "Hard_points"
                ]
                for i in get_points:
                    if i > st.session_state["points"]:
                        change_score = False
                    else:
                        change_score = True

                if change_score:
                    # updates the user's Hard_points score
                    df.loc[
                        df["Username"] == st.session_state["user"], "Hard_points"
                    ] = st.session_state["points"]
                    df.to_csv("user_data/data.csv", index=False)
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
        random_key = random.choice(list(func_dict.keys()))
        equation, answer = func_dict.get(random_key)
        st.session_state["question"] = equation
        st.session_state["ans"] = answer
        # updating the box to display the newly generated question
        question_box.write(
            f"<p>{st.session_state['question']}</p>", unsafe_allow_html=True
        )
        # rerunning the script for the visual effects
        st.rerun()

    # else, an error message is flagged
    else:
        invalid_format.info("Invalid format")
