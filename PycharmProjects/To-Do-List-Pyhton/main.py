To_dos = []

def addToDo():
    to_do = input("Que tarea te gustaria agregar: ")
    To_dos.append(to_do) #Metodo para agregar valores a los arreglos
    print(To_dos)

while True:
    addToDo()