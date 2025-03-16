import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")
label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
label3 = sg.Text("", key="result")

window = sg.Window("Feet and inches to CM by ESuances",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, label3]])
while True:
    event, values = window.read()
    match event:
        case "Convert":
            if values["feet"] != "" and values["inches"] != "":
                feet_to_convert = float(values["feet"])
                inches_to_convert = float(values["inches"])
                feet_result = feet_to_convert * 30.48
                inches_result = inches_to_convert * 2.54
                result = feet_result + inches_result
                window["result"].update(value=f"The convertion to cm is: {result}")
            else:
                window["result"].update(value="Please, make sure to provide all the values", text_color="red")
        case sg.WIN_CLOSED:  # When the window is closed by the user
            break
window.close()