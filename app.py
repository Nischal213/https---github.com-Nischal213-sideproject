import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from SecurePassword import SecurePassword
from email_validator import validate_email, EmailNotValidError

st.set_page_config(page_title="Math Maestro | Register Page")

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = pd.read_csv("main_data/data.csv")


def is_username_valid(username):

    def has_invalid_chars(word):
        # Only accepts one special character "_"
        # All the other special characters are rejected
        return not (all((i == "_" or i.isalnum() for i in word)))

    def is_username_unique(username):
        return all(i != username for i in df["Username"])

    def only_numbers(word):
        return all(i.isdigit() for i in word)

    def only_one_underscode(word):
        return word.count("_")

    error_msg = ""
    if username:
        if is_username_unique(username) == False:
            error_msg = "Username already taken"
            return (False, error_msg)
        elif not (3 <= len(username) <= 20):
            error_msg = "Username can only be 3-20 chars long"
            return (False, error_msg)
        elif has_invalid_chars(username) == True:
            error_msg = "Username may only contain letters, numbers and _"
            return (False, error_msg)
        elif only_numbers(username):
            error_msg = "Username may contain private information"
            return (False, error_msg)
        elif only_one_underscode(username) > 1:
            error_msg = "Username may at most have one _"
            return (False, error_msg)
        else:
            return (True, error_msg)
    else:
        return ("", error_msg)


def is_password_valid(password):

    def has_special_chars(word):
        return not (all(i.isalnum() for i in word))

    def has_upper_chars(word):
        return any(i.isupper() for i in word)

    def has_lower_chars(word):
        return any(i.islower() for i in word)

    error_msg = ""
    if password:
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
    else:
        return ("", error_msg)


def is_email_valid(email):

    def does_email_exist(email):
        try:
            verify = validate_email(email)
            return True
        except EmailNotValidError:
            return False

    def is_email_taken(email):
        return any(i == email for i in df["Email"])

    error_msg = ""
    if email:
        if does_email_exist(email) == False:
            error_msg = "Email does not exist"
            return (False, error_msg)
        elif is_email_taken(email) == True:
            error_msg = "Email already in use"
            return (False, error_msg)
        else:
            return (True, error_msg)
    else:
        return ("", error_msg)


st.image("static/header.png")
username = st.text_input(
    "Username", max_chars=20, placeholder="Enter a unique username"
)
user_result, user_error = is_username_valid(username)
if user_result == False:
    st.error(f"{user_error}")
password = st.text_input(
    "Password", type="password", placeholder="Enter your password", max_chars=55
)
pass_result, pass_error = is_password_valid(password)
if pass_result == False:
    st.error(f"{pass_error}")
email = st.text_input("Email", max_chars=100, placeholder="Enter a valid email")
email_result, email_error = is_email_valid(email)
if email_result == False:
    st.error(f"{email_error}")
submit_button = st.button("Sign Up", type="primary")
st.markdown(
    "<div id = 'has_account'><p> Already have an account? click <a href='/login_page' target='_self'>Here</a></p></div>",
    unsafe_allow_html=True,
)
if submit_button:
    if user_result == True and email_result == True and pass_result == True:
        instance = SecurePassword(password)
        secure_password = instance.secure()
        if "user" not in st.session_state:
            st.session_state["user"] = username
        # Updating the csv file by adding the details of the
        # registered user
        with open("main_data/data.csv", "a") as f:
            f.write(f"{username},{secure_password},{email},0,0,0,False")
            f.write("\n")
        # Making the user's own csv file which is used to keep
        # track of their personal score
        with open(f"user_data/{username}.csv", "w") as f:
            f.write(f"Points,Date")
        switch_page("login page")
    else:
        st.warning("Not all the fields are valid")
