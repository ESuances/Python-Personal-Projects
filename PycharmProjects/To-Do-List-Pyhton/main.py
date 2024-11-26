to_dos = []

while True:
    desicion = input("Type add or show, or exit: ")
    desicion = desicion.strip()

    match desicion:
        case "add":
            to_do = input("Enter a to do: ")
            to_dos.append(to_do)
        case "show":
            for x in to_dos:
                print(x.capitalize())
        case "exit":
            break
        case _:
            print("Pusiste algo que nada que ver loco")

print("Bye!")