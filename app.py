import streamlit as st
import os
import string


def is_username_valid(username):

    def has_invalid_chars(str):
        return not (
            [i for i in str if (i in string.punctuation and i != "_") or i.isspace()]
        )

    def is_username_unique(str):
        return not (
            [i for i in os.listdir("user_data") if i.removesuffix(".txt") == username]
        )

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
username = st.text_input(
    "Username", placeholder="Enter a unique username", max_chars=20
)
result, msg = is_username_valid(username)
if result == False:
    st.error(f"{msg}")
