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


def has_special_chars(str):
    return bool([i for i in str if i in string.punctuation])


def is_password_valid(password):

    def has_upper_chars(str):
        return bool([i for i in str if i.isupper()])

    def has_lower_chars(str):
        return bool([i for i in str if i.islower()])

    error_msg = ""
    if len(password) < 8:
        error_msg = "Password is too short"
        return (False, error_msg)
    elif has_special_chars(password) == False:
        error_msg = "Password must have a special character"
        return (False, error_msg)
    elif has_lower_chars(password) == False:
        error_msg = "Password must have at least 1 lowercase letter"
        return (False, error_msg)
    elif has_upper_chars(password) == False:
        error_msg = "Password must have at least 1 uppercase letter"
        return (False, error_msg)
    else:
        return (True, error_msg)


def is_email_valid(email):
    # Function to check if an email string is valid
    if has_special_chars(email):
        # Checks if the email string contains at least 1 '.' and only 1 '@'
        if email.count(".") != 0 and email.count("@") == 1:
            # Checks if there is anything before the '@' symbol
            before_at_symbol = len(email[: email.index("@")])
            # Checks if there is anything after the '@'symbol
            after_at_symbol = len(email[email.index("@") + 1 :])
            if before_at_symbol > 0 and after_at_symbol > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


st.write("Hello world")
username = st.text_input(
    "Username", placeholder="Enter a unique username", max_chars=20
)
username_error_box = st.empty()
password = st.text_input("Password", placeholder="Enter a password", type="password")
password_error_box = st.empty()
email = st.text_input("Email", placeholder="Enter your email", max_chars=100)
email_error_box = st.empty()
submit = st.button("Sign Up")
if submit:
    username_result, username_error_msg = is_username_valid(username)
    if username_result == False:
        username_error_box.text(f"{username_error_msg}")
    password_result, password_error_msg = is_password_valid(password)
    if password_result == False:
        password_error_box.text(f"{password_error_msg}")
    email_result = is_email_valid(email)
    if email_result == False:
        email_error_box.text("Invalid email address")
