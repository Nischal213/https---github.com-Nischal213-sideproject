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

import random
import ssl
import smtplib
from email.message import EmailMessage

email_sender = "mathsmaestro123@gmail.com"
email_password = "mnwg homw fgap fika"
email_receiver = "krishnakumra0116@yahoo.com"
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
