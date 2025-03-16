import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="to_do")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_to_dos(), key="to_dos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My To Do App",
                   layout=[[label, input_box, add_button],
                   [list_box, edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            if values["to_do"] != "": # We make sure that the user is not posting something empty
                to_dos = functions.get_to_dos() # We get the current values of the list
                new_to_do = values["to_do"] + '\n' # We get the current text on the textbox, we get this from its key
                to_dos.append(new_to_do) # We add the current to do value
                functions.write_to_dos(to_dos) # We write the list
                window['to_dos'].update(values=to_dos) # We update the values so that it is displayed in the screen
        case "Edit":
            if values["to_do"] != "": # Again, we check that there is no empty edits in this case
                to_do_to_edit = values['to_dos'][0] # We get the value from the list
                new_to_do = values['to_do'] + '\n' # We get the new to do
                to_dos = functions.get_to_dos() # We get the actual backend list
                index = to_dos.index(to_do_to_edit) # We get the index of the to do we wish to edit
                to_dos[index] = new_to_do # We set the new value with the index
                functions.write_to_dos(to_dos) # We write the backend list
                window['to_dos'].update(values=to_dos) # We display the new backend list.
        case 'to_dos': # With this we can get an event when the user clicks on a list element
            window['to_do'].update(value=values['to_dos'][0]) # We update the text box so that if the user wants to edit it, its already there to edit.
        case sg.WIN_CLOSED: # When the window is closed by the user
            break
window.close()