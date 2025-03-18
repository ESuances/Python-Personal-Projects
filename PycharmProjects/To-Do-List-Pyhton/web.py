import streamlit as st
import functions

to_dos = functions.get_to_dos()

def add_todo():
    new_to_do = st.session_state["AddToDoTextBox"]
    if new_to_do != "":
        to_dos = functions.get_to_dos()
        to_dos.append(new_to_do + '\n')
        functions.write_to_dos(to_dos)


st.title("My To do App")
st.subheader("This is my to do app")
st.write("This app was made to increase your productivity")

for index, to_do in enumerate(to_dos):
    checkbox = st.checkbox(to_do, key=to_do)
    if checkbox:
        to_dos.pop(index)
        functions.write_to_dos(to_dos)
        del st.session_state[to_do]
        st.rerun()

st.text_input(label="", placeholder="Add a new to do... when you're done, hit enter :) ", on_change=add_todo, key="AddToDoTextBox")
