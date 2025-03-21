import streamlit as st

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/MyCurrentProfile.png", width=1500)

with col2:
    st.title("Welcome to my first portafolio")
    content = """Hi, I'm Erick Suances, a Mechatronics/Software engineer that loves to code, I have multiple projects going on, mainly I do
    game develpoment and small React Native applications, but I also have experience in big and scalable applications Using PHP Laravel as backend with MySQL
    and React as the Front End."""
    st.info(content)

st.text("Below you can find some of the apps I have built in Python. Feel free to contact me!")