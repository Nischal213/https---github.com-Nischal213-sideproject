import streamlit as st

# custom styling
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write(
    "<h1>401 Error , You must be logged in </h1>",
    unsafe_allow_html=True,
)

st.write(
    "<div id = 'header_error'><h4>Click <a href='http://localhost:8501/login_page' target='_self'> here </a> to be redirected to the main page </h4></div>",
    unsafe_allow_html=True,
)

import streamlit as st
import random
import pandas as pd
import ssl
import smtplib
from email.message import EmailMessage
from streamlit_extras.switch_page_button import switch_page

if "user" not in st.session_state:
    switch_page("error page")


if "verification_code" not in st.session_state:
    df = pd.read_csv("main_data/data.csv")
    # get_email = df.loc[df["Username"] == f"{st.session_state["user"]}", "Email"]
    # email_receiver = f"{get_email.values[0]}"
    email_sender = "mathsmaestro123@gmail.com"
    email_password = "mnwg homw fgap fika"
    email_receiver = "n_gurung18@cranford.hounslow.sch.uk"
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
        print("Sucesss")
    st.session_state["verification_code"] = random_code
    print(random_code)

st.header("Verify it's you")
verify_code = st.text_input(
    "Enter the verification code sent to your email",
    max_chars=6,
)
check_button = st.button("Submit code")
if check_button:
    if verify_code == st.session_state["verification_code"]:
        switch_page("home")
    else:
        st.warning("INCORRECT PIN AHHHHHHHHHHHHHHHHHHHH")

