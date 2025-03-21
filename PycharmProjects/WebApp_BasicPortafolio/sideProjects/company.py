import streamlit as st
import pandas

st.set_page_config(layout="wide")
col5, col6 = st.columns([2.0,0.5])

col1, col2 , col3 = st.columns(3)

with col5:
    st.title("The Best Company")
    st.write("akjdmkasmdasodjiasoidaoidoaskdosaokdoiasndoiasoidmasoidmoasmdoasodmasodoasmdoasmdoasmdoasdoasmdoaoidnonojonduenaiunsdoagoiasngoiasnd asoid sdjoa saooos jdas hdoasuhduashd ashdoia oaoi ashdo asoia oia soas hdoashdi")
    st.title("Our Team")

df = pandas.read_csv("sideProjects/data_exercise.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        name = f"{row['firstname']} {row['lastname']}".title()
        st.header(f"{name}")
        st.write(row['role'])
        st.image("sideProjects/images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        name = f"{row['firstname']} {row['lastname']}".title()
        st.header(f"{name}")
        st.write(row['role'])
        st.image("sideProjects/images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        name = f"{row['firstname']} {row['lastname']}".title()
        st.header(f"{name}")
        st.write(row['role'])
        st.image("sideProjects/images/" + row['image'])