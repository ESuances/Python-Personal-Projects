import streamlit as st
import pandas

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/MyCurrentProfile.png", width=2000)

with col2:
    st.title("Welcome to my first Python Portafolio")
    content = """Hi, I'm Erick Suances, a Mechatronics/Software engineer that loves to code, I have multiple projects going on, mainly I do
    game develpoment and small React Native applications, but I also have experience in big and scalable applications Using PHP Laravel as backend with MySQL
    and React as the Front End."""
    st.info(content)

st.text("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, AuxCol, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f'[Source Code]({row['url']})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f'[Source Code]({row['url']})')
