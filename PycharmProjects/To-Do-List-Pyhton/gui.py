import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="to_do")
add_button = sg.Button("Add")

window = sg.Window("My To Do App",
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            to_dos = functions.get_to_dos()
            new_to_do = values["to_do"] + '\n'
            to_dos.append(new_to_do)
            functions.write_to_dos(to_dos)
        case sg.WIN_CLOSED:
            break
window.close()