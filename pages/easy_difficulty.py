import streamlit as st
import random
from streamlit_extras.switch_page_button import switch_page


def generate_random_questions():
    question = []
    for i in range(10):
        random_op = random.choice(["+", "-", "*", "/"])
        if random_op in ["/" , "*"]:
            num1, num2 = random.randint(1, 10), random.randint(1, 10)
        else:
            num1, num2 = random.randint(1, 100), random.randint(1, 100)
        answer = round(eval(f"{num1} {random_op} {num2}"), 1)
        tuple = (num1, random_op, num2, answer)
        question.append(tuple)
    return question


with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    "<div id = 'sub-header'><h2><span style='color:green;'>Easy Difficulty</h2></span></div>",
    unsafe_allow_html=True,
)
question_list = generate_random_questions()
num1 , random_op , num2 , answer = question_list[0][0] , question_list[0][1] , question_list[0][2] , question_list[0][3]
st.markdown('<span id="question"></span>', unsafe_allow_html=True)
st.write(f"What is {num1} {random_op} {num2}?")
user_answer = st.text_input("")
