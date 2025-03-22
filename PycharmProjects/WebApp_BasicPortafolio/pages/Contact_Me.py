import streamlit as st
from send_email import sendEmail

st.header("Contact Me")
st.write("If you're interested in my work, please, send me a message, I'll gladly response as soon as possible.")

with st.form(key='ContactForm'):
    user_email = st.text_input("Your Email address")
    user_message = st.text_area("Your message")
    message = f"""\
Subject: New Email from {user_email}

Email received from {user_email}
{user_message}
    """
    button = st.form_submit_button("Send")
    if button:
        sendEmail(message)
        st.info("Your Email was sent successfully, I'll respond as soon as posible, Thanks!")
