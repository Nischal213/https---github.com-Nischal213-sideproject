import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd


def home_page():
    st.markdown(
        "<div id = 'header'><h1>Welcome to</h1></div>",
        unsafe_allow_html=True,
    )
    st.image("static/game_logo.png")
    st.markdown(
        "<div id = 'sub-header'><h2>Pick a difficulty</h2></div>",
        unsafe_allow_html=True,
    )

    # game difficulty descriptions
    with open("static/difficulty.html") as f:
        st.markdown(f"{f.read()}", unsafe_allow_html=True)

    st.markdown('<span id="easy-button"></span>', unsafe_allow_html=True)
    easy_mode = st.button("Play!", key="easy")
    st.markdown('<span id="medium-button"></span>', unsafe_allow_html=True)
    medium_mode = st.button("Play!", key="medium")
    st.markdown('<span id="hard-button"></span>', unsafe_allow_html=True)
    hard_mode = st.button("Play!", key="hard")

    if easy_mode:
        switch_page("easy difficulty")

    if medium_mode:
        switch_page("medium difficulty")

    if hard_mode:
        switch_page("hard difficulty")


def leaderboards():

    def combine_lists(arr1, arr2):
        new_list = []
        for i in range(len(arr1)):
            new_list.append((arr1[i], arr2[i]))
        return new_list

    def easy():
        extracted_df = df[["Username", "Easy_points"]].sort_values(
            by="Easy_points", ascending=False
        )
        top_3_usernames = list(extracted_df[:3]["Username"])
        top_3_points = list(extracted_df["Easy_points"])
        count = 0
        content = ""
        for i, j in combine_lists(top_3_usernames, top_3_points):
            st.markdown('<span id="leaderboards"></span>', unsafe_allow_html=True)
            if count == 0:
                content += f"🥇<span style='color:#FFD700;' id='leaderboards'>{i} scored {int(j)} in easy difficulty</span>"
            elif count == 1:
                content += f"🥈<span style='color:#C0C0C0;' id='leaderboards'>{i} scored {int(j)} in easy difficulty</span>"
            elif count == 2:
                content += f"🥉<span style='color:#CD7F32 ;'id='leaderboards'>{i} scored {int(j)} in easy difficulty</span>"
            count += 1
        return content

    def medium():
        extracted_df = df[["Username", "Medium_points"]].sort_values(
            by="Medium_points", ascending=False
        )
        top_3_usernames = list(extracted_df[:3]["Username"])
        top_3_points = list(extracted_df["Medium_points"])
        count = 0
        for i, j in combine_lists(top_3_usernames, top_3_points):
            st.markdown('<span id="leaderboards"></span>', unsafe_allow_html=True)
            if count == 0:
                st.write(
                    f"🥇<span style='color:#FFD700;'>{i} scored {int(j)} in medium difficulty</span>",
                    unsafe_allow_html=True,
                )
            elif count == 1:
                st.write(
                    f"🥈<span style='color:#C0C0C0;'>{i} scored {int(j)} in medium difficulty</span>",
                    unsafe_allow_html=True,
                )
            elif count == 2:
                st.write(
                    f"🥉<span style='color:#CD7F32 ;'>{i} scored {int(j)} in medium difficulty</span>",
                    unsafe_allow_html=True,
                )
            count += 1
        return ""

    def hard():
        extracted_df = df[["Username", "Hard_points"]].sort_values(
            by="Hard_points", ascending=False
        )
        top_3_usernames = list(extracted_df[:3]["Username"])
        top_3_points = list(extracted_df["Hard_points"])
        count = 0
        for i, j in combine_lists(top_3_usernames, top_3_points):
            st.markdown('<span id="leaderboards"></span>', unsafe_allow_html=True)
            if count == 0:
                st.write(
                    f"🥇<span style='color:#FFD700;'>{i} scored {int(j)} in hard difficulty</span>",
                    unsafe_allow_html=True,
                )
            elif count == 1:
                st.write(
                    f"🥈<span style='color:#C0C0C0;'>{i} scored {int(j)} in hard difficulty</span>",
                    unsafe_allow_html=True,
                )
            elif count == 2:
                st.write(
                    f"🥉<span style='color:#CD7F32 ;'>{i} scored {int(j)} in hard difficulty</span>",
                    unsafe_allow_html=True,
                )
            count += 1
        return ""

    df = pd.read_csv("user_data/data.csv")
    st.markdown('<span id="lb-header"></span>', unsafe_allow_html=True)
    st.write("Leaderboards")
    if "show_default" not in st.session_state:
        st.session_state["show_default"] = True
    st.markdown('<span id="lb-box"></span>', unsafe_allow_html=True)
    lb_box = st.empty()
    if st.session_state["show_default"]:
        lb_box.write("Press a button below to show the corresponding leaderboards")
        st.session_state["show_default"] = False
    st.markdown('<span id="easy-btn"></span>', unsafe_allow_html=True)
    btn_easy = st.button("Easy")
    st.markdown('<span id="medium-btn"></span>', unsafe_allow_html=True)
    btn_medium = st.button("Medium")
    st.markdown('<span id="hard-btn"></span>', unsafe_allow_html=True)
    btn_hard = st.button("Hard")
    if btn_easy:
        content = easy()
        print(content)
        lb_box.text(content)

    if btn_medium:
        lb_box.write(medium())

    if btn_hard:
        lb_box.write(hard())


# if "user" not in st.session_state:
#     switch_page("error page")

st.set_page_config(page_title="Math Maestro | Game Page")


# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

pages = ["Home", "Leaderboards"]

tabs = st.tabs(pages)

with tabs[0]:
    home_page()

with tabs[1]:
    leaderboards()
