import streamlit as st
import functions

to_dos = functions.get_to_dos()

def add_todo():
    new_to_do = st.session_state["AddToDoTextBox"]
    if new_to_do != "":
        to_dos = functions.get_to_dos()
        to_dos.append(new_to_do + '\n')
        functions.write_to_dos(to_dos)
    st.session_state["AddToDoTextBox"] = ""


st.title("My To do App")
st.subheader("This is my to do app")
st.write("This app was made to increase your productivity")

for to_do in to_dos:
    st.checkbox(to_do)

st.text_input(label="", placeholder="Add a new to do... when you're done, hit enter :) ", on_change=add_todo, key="AddToDoTextBox")
