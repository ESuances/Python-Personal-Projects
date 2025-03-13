def get_to_dos(filepath="to_dos.txt"): # This way, the function already has a default parameter
    """Function to get access to the text file and get the current information on that text file"""
    with open(filepath, "r") as file_local:
        to_dos_local = file_local.readlines()
    return to_dos_local

def write_to_dos(to_dos_local, filepath="to_dos.txt"): # If there is an argument without a default parameter, to fix the error, just put it first.
    """Function to write new information on the to_dos text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(to_dos_local)

def printOutTo_dos(to_dos_local):
    """Function to printout the current information of a list, but more specifically for a list of to dos"""
    for index, x in enumerate(to_dos_local):
        x = x.strip('\n')
        print(f"{index + 1}. {x.capitalize()}")

def add_to_dos(decision_local):
    """Function to add to dos to the to_dos.txt file."""
    to_do = decision_local[4:]
    to_dos = get_to_dos() # Since we have a default parameter, we don't need to add the argument if the default is correct.
    to_dos.append(to_do + '\n')
    write_to_dos(to_dos)

def show_to_dos():
    """Function to get the information of the text file and print it out on console."""
    to_dos = get_to_dos()
    printOutTo_dos(to_dos)

def edit_to_dos(decision):
    """Function to edit a to_do from the to_dos.txt"""
    try:  # Error handling
        to_dos = get_to_dos()
        printOutTo_dos(to_dos)
        edit_to_do = int(input("Enter the number of the to do you wish to edit: "))
        edit_to_do = edit_to_do - 1
        new_to_do = decision[5:]
        to_dos[edit_to_do] = new_to_do + '\n'
        write_to_dos(to_dos)
        print("The new list now looks like this: ")
        printOutTo_dos(to_dos)
    except ValueError:  # Cuando el user ingresa un valor no aceptado, se muestra este error
        print("Your command is not valid, please try again.")

def complete_to_dos():
    """A function to delete or set as complete a to do from the to_dos.txt file"""
    try:
        to_dos = get_to_dos("to_dos.txt")
        printOutTo_dos(to_dos)
        item_to_remove = int(input("Enter the number of the task you completed: "))
        to_dos.pop(item_to_remove - 1)
        write_to_dos(to_dos)
        print("Great, well done, now the list looks like this: ")
        printOutTo_dos(to_dos)
    # Error handling, making sure if the program gets into any error, we let the user know
    except ValueError:  # If the user types an invalid type, for example a letter
        print("Your command is not valid, please try again.")
    except IndexError:  # If the number is not on the range of the array
        print("The inputed number is not on the list, pleaase try again.")
