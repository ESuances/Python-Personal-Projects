
while True:
    desicion = input("Type add or show, edit, complete or exit: ")
    desicion = desicion.strip()

    match desicion:
        case "add":
            to_do = input("Enter a to do: ") + "\n"
            file = open('to_dos.txt','r') # We create a read first to get its values
            file.close() # It is better to close the file once we already have the information stored in the file variable
            to_dos = file.readlines() # We assign the values that were already there to the list
            to_dos.append(to_do) # We provide the added to do to the RAM
            file = open('to_dos.txt','w')  # We open the file again, this time to write the added to do.
            file.writelines(to_dos) # We write the file with all of the new information
            file.close() # Again, once we write the new info in the file, we once again close it.
        case "show":
            file = open('to_dos.txt', 'r')
            to_dos = file.readlines()
            file.close()
            #new_to_do = [item.strip('\n') for item in to_dos] Previous code to remove the gap between items
            for index, x in enumerate(to_dos):
                x = x.strip('\n')
                print(f"{index + 1}. {x.capitalize()}")
        case "edit":
            for index, x in enumerate(to_dos):
                print(f"{index + 1}. {x.capitalize()}")
            edit_to_do = int(input("Enter the number of the to do you wish to edit: "))
            edit_to_do = edit_to_do - 1
            new_to_do = input("Enter the new to do: ")
            to_dos[edit_to_do] = new_to_do
            Amount_of_to_dos = 0
            print("The new list now looks like this: ")
            for x in to_dos:
                Amount_of_to_dos = Amount_of_to_dos + 1
                print(f"{Amount_of_to_dos}. {x.capitalize()}")
        case "complete":
            for index, x in enumerate(to_dos):
                print(f"{index + 1}. {x.capitalize()}")
            item_to_remove = int(input("Enter the number of the task you completed: "))
            to_dos.pop(item_to_remove - 1)
            print("Great, well done, now the list looks like this: ")
            for index, x in enumerate(to_dos):
                print(f"{index + 1}. {x.capitalize()}")
        case "exit":
            break
        case _:
            print("Pusiste algo que nada que ver loco")

print("Bye!")