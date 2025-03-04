to_dos = []

while True:
    desicion = input("Type add or show, edit or exit: ")
    desicion = desicion.strip()

    match desicion:
        case "add":
            to_do = input("Enter a to do: ")
            to_dos.append(to_do)
        case "show":
            for x in to_dos:
                print(x.capitalize())
        case "edit":
            edit_to_do = int(input("Enter the number of the to do you wish to edit: "))
            edit_to_do = edit_to_do - 1
            new_to_do = input("Enter the new to do: ")
            to_dos[edit_to_do] = new_to_do
            print(to_dos[edit_to_do])
        case "exit":
            break
        case _:
            print("Pusiste algo que nada que ver loco")

print("Bye!")