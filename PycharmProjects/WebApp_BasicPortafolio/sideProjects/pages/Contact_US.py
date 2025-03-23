import streamlit as st

st.header("Contact Us")

with st.form(key='ContactUsForm'):
    sender_email = st.text_input("Your email address")
    option = st.selectbox(
        "What topic would you need to discuss?",
        ("Job Inquires", "Job Proposals", "Other"),
    )
    sender_message = st.text_area("Your message")
    button = st.form_submit_button("Send")
    # if button: If we wanted to add functionality to this page
    # Since we don't here refer to Contact_Me.py under pages/Contact_Me.py