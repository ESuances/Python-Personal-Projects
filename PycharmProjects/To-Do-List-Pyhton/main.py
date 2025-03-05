to_dos = []

while True:
    desicion = input("Type add or show, edit, complete or exit: ")
    desicion = desicion.strip()

    match desicion:
        case "add":
            to_do = input("Enter a to do: ")
            to_dos.append(to_do)
        case "show":
            for index, x in enumerate(to_dos):
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