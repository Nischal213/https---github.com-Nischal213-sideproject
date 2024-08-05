import streamlit as st
import random
import pandas as pd
import ssl
import smtplib
from SecurePassword import SecurePassword
from email.message import EmailMessage
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="Math Maestro | Forgot Page")

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


if "temp_user" not in st.session_state:
    switch_page("error page")

df = pd.read_csv("main_data/data.csv")

if "verification_code" not in st.session_state:
    # This entire block of code makes an email
    # along with a random 6-digit PIN sent
    # to the user's registered email address
    email_sender = "mathsmaestro123@gmail.com"
    email_password = "mnwg homw fgap fika"
    get_email = df.loc[df["Username"] == f"{st.session_state['temp_user']}", "Email"]
    email_receiver = f"{get_email.values[0]}"
    random_code = "".join([str(random.randint(0, 9)) for i in range(6)])

    subject = "Maths Maestro Verification Code"
    body = f"""
    Hello,

    This is your 6-digit verification code:
    {random_code}
    Make sure to not let anyone else know this code

    Sincerely,
    Maths Maestro
    """
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    st.session_state["verification_code"] = random_code


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


st.header("Verify it's you")
new_password = st.text_input(
    "New password",
    type="password",
    placeholder="Enter a new password",
    max_chars=55,
)
verify_code = st.text_input(
    "Enter the verification code sent to your email",
    max_chars=6,
)

submit = st.button("Submit", type="primary")
if submit:
    pass_result, pass_error = is_password_valid(new_password)
    if verify_code == st.session_state["verification_code"] and pass_result:
        st.session_state["user"] = st.session_state["temp_user"]
        del st.session_state["temp_user"]
        instance = SecurePassword(new_password)
        # Updating the old password with the new hashed password
        df.loc[df["Username"] == f"{st.session_state['user']}", "Password"] = (
            instance.secure()
        )
        df.to_csv("main_data/data.csv", index=False)
        switch_page("home")
    elif verify_code != st.session_state["verification_code"]:
        st.error("Incorrect PIN entered , please try again")
    else:
        st.error(f"{pass_error}")
