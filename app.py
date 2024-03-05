import streamlit as st
import os
import string

with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def is_username_valid(username):

    def has_invalid_chars(str):
        return not (
            [i for i in str if (i in string.punctuation and i != "_") or i.isspace()]
        )

    def is_username_unique(str):
        return not (
            [i for i in os.listdir("user_data") if i.removesuffix(".txt") == str]
        )
        # Uses list comprehension to iterate over all files within the folder user_data
        # If the username is matching with the name of one of the files , it is appended.
        # An empty list means that the username is unique
        # The list is converted to a boolean value so an empty list becomes 0 whilst
        # a non empty list becomes 1

    error_msg = ""
    if is_username_unique(username) == False:
        error_msg = "Username already taken."
        return (False, error_msg)
    elif len(username) > 20 or len(username) < 3:
        error_msg = "Username can only be 3-20 chars long."
        return (False, error_msg)
    elif has_invalid_chars(username) == False:
        error_msg = "Username may only contain letters, numbers and _."
        return (False, error_msg)
    elif len([i for i in username if i in string.digits]) == len(username):
        error_msg = "Username may contain private information"
        return (False, error_msg)
    else:
        return (True, error_msg)


st.write("Hello world")
username = st.text_input("Username")
user_result, user_error = is_username_valid(username)
if len(username) == 0:
    st.info(f"Enter a username")
    user_result = False
else:
    if user_result == False:
        st.error(f"{user_error}")
