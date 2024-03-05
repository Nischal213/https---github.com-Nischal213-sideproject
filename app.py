import streamlit as st
import os
import string
from streamlit_extras.switch_page_button import switch_page

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
        error_msg = "Username already taken"
        return (False, error_msg)
    elif len(username) > 20 or len(username) < 3:
        error_msg = "Username can only be 3-20 chars long"
        return (False, error_msg)
    elif has_invalid_chars(username) == False:
        error_msg = "Username may only contain letters, numbers and _"
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
        error_msg = "Password is must be at least 8 characters long"
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

    def does_email_exist(email):
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

    def is_email_taken(email):
        for i in os.listdir("user_data"):
            with open(f"user_data/{i}", "r") as f:
                content = f.readlines()[2][7:]
                if content == email:
                    return True
        return False

    error_msg = ""
    if does_email_exist(email) == False:
        error_msg = "Email does not exist"
        return (False, error_msg)
    elif is_email_taken(email) == True:
        error_msg = "Email already in use"
        return (False, error_msg)
    else:
        return (True, error_msg)


st.write("Hello world")
username = st.text_input("Username", max_chars=20)
if len(username) == 0:
    st.info(f"Enter a unique username")
    user_result = False
else:
    user_result, user_error = is_username_valid(username)
    if user_result == False:
        st.error(f"{user_error}")
password = st.text_input("Password", type="password")
if len(password) == 0:
    st.info(f"Enter a secure password")
    pass_result = False
else:
    pass_result, pass_error = is_password_valid(password)
    if pass_result == False:
        st.error(f"{pass_error}")
email = st.text_input("Email", max_chars=100)
if len(email) == 0:
    st.info(f"Enter your email")
    email_result = False
else:
    email_result, email_error = is_email_valid(email)
    if email_result == False:
        st.error(f"{email_error}")
submit_button = st.button("Sign Up", type="secondary")
st.markdown(
    "<p> Already have an account? click <a href='/login_page' target='_self'>Here</a></p>",
    unsafe_allow_html=True,
)
if submit_button:
    if user_result == True and email_result == True and pass_result == True:
        st.success("Account Successfully Created")
        with open(f"user_data/{username}.txt", "w") as f:
            f.write(f"Username: {username}\nPassword: {password}\nEmail: {email}")
        switch_page("login page")
    else:
        st.warning("Not all the fields are valid")
