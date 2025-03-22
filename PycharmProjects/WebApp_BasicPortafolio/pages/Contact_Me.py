import streamlit as st

st.header("Contact Me")
st.write("If you're interested in my work, please, send me a message, I'll gladly response as soon as possible.")

with st.form(key='ContactForm'):
    user_email = st.text_input("Your Email address")
    user_message = st.text_area("Your message")
    button = st.form_submit_button("Send")
    #if button:

