lista=[]
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista según el índice")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista según el nombre (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")
def ingresar_elemento():
    elemento = input("Ingrese el elemento a la lista: ")
    lista.append(elemento)
    print(f"Elemento '{elemento}' agregado a la lista.")
def modificar_elemento():
    try:
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        if 0 <= indice < len(lista):
            nuevo_valor = input("Ingrese el nuevo valor: ")
            lista[indice] = nuevo_valor
            print(f"Elemento en el índice {indice} modificado.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
def eliminar_elemento_por_indice():
    try:
        indice = int(input("Ingrese el índice del elemento a eliminar: "))
        if 0 <= indice < len(lista):
            eliminado = lista.pop(indice)
            print(f"Elemento '{eliminado}' en el índice {indice} eliminado.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
def eliminar_ultimo_elemento():
    if lista:
        eliminado = lista.pop()
        print(f"Último elemento '{eliminado}' eliminado.")
    else:
        print("La lista está vacía.")
def buscar_elemento():
    elemento = input("Ingrese el elemento a buscar: ")
    if elemento in lista:
        indice = lista.index(elemento)
        print(f"Elemento '{elemento}' encontrado en el índice {indice}.")
    else:
        print(f"Elemento '{elemento}' no encontrado en la lista.")
def mostrar_todos_los_elementos():
    if lista:
        print("Elementos de la lista:")
        for i, elemento in enumerate(lista):
            print(f"{i}: {elemento}")
    else:
        print("La lista está vacía.")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ")
    
    if opcion == '1':
        ingresar_elemento()
    elif opcion == '2':
        modificar_elemento()
    elif opcion == '3':
        eliminar_elemento_por_indice()
    elif opcion == '4':
        eliminar_ultimo_elemento()
    elif opcion == '5':
        buscar_elemento()
    elif opcion == '6':
        mostrar_todos_los_elementos()
    elif opcion == '7':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")