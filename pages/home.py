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
        combined_lst = combine_lists(top_3_usernames, top_3_points)
        st.write(
            f"""
            <div class = 'easy-dif' >
                <div>
                    🥇<span style='color:#FFD700;' id='leaderboards'>
                    {combined_lst[0][0]} scored {int(combined_lst[0][1])} points in easy difficulty
                    </span>
                </div>
                <div>
                    🥈<span style='color:#C0C0C0;' id='leaderboards'>
                    {combined_lst[1][0]} scored {int(combined_lst[1][1])} points in easy difficulty
                    </span>
                </div>
                <div>
                    🥉<span style='color:#CD7F32;' id='leaderboards'>
                    {combined_lst[2][0]} scored {int(combined_lst[2][1])} points in easy difficulty
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def medium():
        extracted_df = df[["Username", "Medium_points"]].sort_values(
            by="Medium_points", ascending=False
        )
        top_3_usernames = list(extracted_df[:3]["Username"])
        top_3_points = list(extracted_df["Medium_points"])
        combined_lst = combine_lists(top_3_usernames, top_3_points)
        st.write(
            f"""
            <div class = 'medium-dif'>
                <div>
                    🥇<span style='color:#FFD700;' id='leaderboards'>
                    {combined_lst[0][0]} scored {int(combined_lst[0][1])} points in medium difficulty
                    </span>
                </div>
                <div>
                    🥈<span style='color:#C0C0C0;' id='leaderboards'>
                    {combined_lst[1][0]} scored {int(combined_lst[1][1])} points in medium difficulty
                    </span>
                </div>
                <div>
                    🥉<span style='color:#CD7F32;' id='leaderboards'>
                    {combined_lst[2][0]} scored {int(combined_lst[2][1])} points in medium difficulty
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def hard():
        extracted_df = df[["Username", "Hard_points"]].sort_values(
            by="Hard_points", ascending=False
        )
        top_3_usernames = list(extracted_df[:3]["Username"])
        top_3_points = list(extracted_df["Hard_points"])
        combined_lst = combine_lists(top_3_usernames, top_3_points)
        st.write(
            f"""
            <div class = 'hard-dif'>
                <div>
                    🥇<span style='color:#FFD700;' id='leaderboards'>
                    {combined_lst[0][0]} scored {int(combined_lst[0][1])} points in hard difficulty
                    </span>
                </div>
                <div>
                    🥈<span style='color:#C0C0C0;' id='leaderboards'>
                    {combined_lst[1][0]} scored {int(combined_lst[1][1])} points in hard difficulty
                    </span>
                </div>
                <div>
                    🥉<span style='color:#CD7F32;' id='leaderboards'>
                    {combined_lst[2][0]} scored {int(combined_lst[2][1])} points in hard difficulty
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    df = pd.read_csv("user_data/data.csv")
    st.markdown('<span id="lb-header"></span>', unsafe_allow_html=True)
    st.write("Leaderboards")
    if "position" not in st.session_state:
        st.session_state["position"] = 0
    st.markdown('<span id="initial-text"></span>', unsafe_allow_html=True)
    easy()
    st.markdown("<span id='next-btn'></span>", unsafe_allow_html=True)
    btn = st.button("Next")
    if btn:
        st.markdown(
            """
        <style>
            .element-container:has(#initial-text) + div {
                display: none;
            }
            .element-container:has(#next-btn) + div button {
                position: fixed;
                transform: translate(20rem , 7rem);
            }
            .element-container:has(#next-btn) + div button:hover {
                border-color: #7F00FF;
                color: #7F00FF;
            }
            .element-container:has(#next-btn) + div button:active {
                background-color: #7F00FF;
                color: white;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.session_state["position"] += 1
        if st.session_state["position"] > 2:
            st.session_state["position"] = 0

        if st.session_state["position"] == 0:
            easy()
        elif st.session_state["position"] == 1:
            medium()
        elif st.session_state["position"] == 2:
            hard()


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
