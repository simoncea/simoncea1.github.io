# Lista de tareas editable
# este programa permite al susio gestionar una lista de tareas.
# El programa permitirá al usuario agregar tareas, marcarlas como pletas y ver la lista de pendientes.


#Inicialista una lista ( array en otros lenguajes) vacía, para almacenar las tareas
lista_de_tareas = []

#funcion para agregar una tarea a la lista
def agregar_tarea():
    tarea =input("Ingrese una nueva tarea: ")
    lista_de_tareas.append(tarea)
    print ("listo, su tarea se agregó correctamente.")

# funcion para agregar todas las tareas de una lista
def mostrar_tarea():
    if not lista_de_tareas:
        print("aca no hay tareas")
    else:
        print("Tareas Pendientes: ")
        for idx, tarea in enumerate(lista_de_tareas, start=1):
            print(f"{idx}. {tarea}")

# funcion para eliminar una tarea de la lista
def eliminar_tarea():
    mostrar_tarea()
    if lista_de_tareas:
        try:
            indice = int(input("ingrese el numero de la tarea que deseas eliminar. "))
            if 1<= indice <= len(lista_de_tareas):
                tarea_eliminada = lista_de_tareas.pop(indice -1)
                print ("La tarea fue eliminada correctamente")
            else:
                print("Numero de tarea no valido")
        except ValueError:
            print("Entrada no válida, debes ingresar un numero")  
    else:
        print("No hay tareas para eliminar")              

#funcion principal
def main():
    while True:
        print("\n Lista de tareas")
        print("1. Agregar tarea ")
        print("2. Mostrar Tareas")
        print("3. Eliminar una tarea")
        print("4. Salir")

        opcion =input("Seccliona una opcion :")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tarea()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print ("Adiós")
            break
        else:
            print("Opción no válida, reintente")
    
if __name__ == "__main__":
    main()