
while True:
    desicion = input("Type add or show, edit, complete or exit: ")
    desicion = desicion.strip()

    match desicion:
        case "add":
            to_do = input("Enter a to do: ") + "\n"
            # GOOD THING TO REMEMBER: Every time you read a file, the pointer is set right after the last character
            # Which means, if you try to read two times in a single with open .... , the second one won't work, because the pointer would have to detect added text after previous code was executed.
            # This of course would be a good way to find out if a non-binary file is being edited while the script is running.
            # Anything else, please, only use the read option once and preferably store it in a variable so that you have it in the code after that.
            with open("to_dos.txt", "r") as file:
                to_dos = file.readlines()
            to_dos.append(to_do) # We provide the added to do to the RAM
            with open("to_dos.txt", "w") as file:
                file.writelines(to_dos)
        case "show":
            with open("to_dos.txt", "r") as file:
                to_dos = file.readlines()
            #new_to_do = [item.strip('\n') for item in to_dos] Previous code to remove the gap between items
            for index, x in enumerate(to_dos):
                x = x.strip('\n')
                print(f"{index + 1}. {x.capitalize()}")
        case "edit":
            # We open the to do list .txt to store the values of the file on the variable to_dos
            with open("to_dos.txt","r") as file:
                to_dos = file.readlines()
            # We print out the list so the user knows which to_do to edit
            for index, x in enumerate(to_dos):
                x = x.strip('\n')
                print(f"{index + 1}. {x.capitalize()}")
            # Once the user knows the to_dos and their number, they can pick whichever the want to edit
            edit_to_do = int(input("Enter the number of the to do you wish to edit: "))
            edit_to_do = edit_to_do - 1
            # After the player selects which one to edit, now the user can edit the to_do, asigning the value on new_to_do
            new_to_do = input("Enter the new to do: ")
            # And assigning the value to de selected to_do with edit_to_do and changing the value with the variable new_to_do
            to_dos[edit_to_do] = new_to_do + '\n'
            # We open the file to assign the new values to the .txt list
            with open("to_dos.txt", "w") as file:
                file.writelines(to_dos)
            # We print out the new list so that the user knows how it looks now.
            print("The new list now looks like this: ")
            for index, x in enumerate(to_dos):
                x = x.strip('\n')
                print(f"{index + 1}. {x.capitalize()}")
        case "complete":
            # We open the .txt to get access to the current data on it
            with open("to_dos.txt","r") as file:
                to_dos = file.readlines()
            # We print out the list with the number so that the user knows which one to select
            for index, x in enumerate(to_dos):
                x = x.strip('\n')
                print(f"{index + 1}. {x.capitalize()}")
            # We ask the user which one the user wants to remove
            item_to_remove = int(input("Enter the number of the task you completed: "))
            # We remove it from the array
            to_dos.pop(item_to_remove - 1)
            # We write the .txt file again with the removed item
            with open("to_dos.txt", "w") as file:
                file.writelines(to_dos)
            # We show the user how the list looks after the change.
            print("Great, well done, now the list looks like this: ")
            for index, x in enumerate(to_dos):
                x = x.strip('\n')
                print(f"{index + 1}. {x.capitalize()}")
        case "exit":
            break
        case _:
            print("Pusiste algo que nada que ver loco")

print("Bye!")