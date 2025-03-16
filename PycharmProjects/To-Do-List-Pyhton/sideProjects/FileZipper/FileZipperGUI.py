import FreeSimpleGUI as sg
from ZipCreator import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="FilesToZip")
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
label3 = sg.Text("Name your Zip file: ")
input_box = sg.InputText(tooltip="Enter the zip name", key="zip_name")
choose_button2 = sg.FolderBrowse("Choose", key="DestinationFolder")

compress_button = sg.Button("Compress")

label4 = sg.Text("", key="output")

window = sg.Window("FileZipper by ESuances",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [label3, input_box],
                           [compress_button, label4]])

while True:
    event, values = window.read()
    match event:
        case "Compress":
            if values["zip_name"] != "":
                print(event,values)
                filepaths = values["FilesToZip"].split(";")
                Destination_folder = values["DestinationFolder"]
                archive_name = values["zip_name"]
                make_archive(filepaths, Destination_folder, archive_name)
                window["output"].update(value="Compression completed!")
            else:
                window["output"].update(value="Please add a name to your zip file", text_color="red")
        case sg.WIN_CLOSED:  # When the window is closed by the user
            break

window.close()