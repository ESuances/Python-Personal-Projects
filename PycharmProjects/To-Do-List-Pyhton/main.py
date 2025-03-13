from functions import add_to_dos, show_to_dos, edit_to_dos, complete_to_dos
while True:
    decision = input("Type add or show, edit, complete or exit: ")
    decision = decision.strip()

    if decision.startswith("add"):
        add_to_dos(decision)
    elif decision.startswith("show"):
        show_to_dos()
    elif decision.startswith("edit"):
        edit_to_dos(decision)
    elif decision.startswith("complete"):
        complete_to_dos()
    elif decision.startswith("exit"):
        break
    else:
        print("Pusiste algo que nada que ver loco")

print("Bye!")