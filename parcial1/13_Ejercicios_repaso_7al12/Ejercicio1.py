# Definimos lista con los 8 números y string
lista = [2, 5, 3, 1, 8, 9, 11, 15]

# Recorreremos lista y la imprimimos
def mostrar_lista(lista):
    for i in lista:
        print(i)

# Recorrer lista y devolver string
def string_lista(lista):
    strlista = "".join(str(i) for i in lista)
    return strlista

# Ordenamos la lista y la imprimimos
def ordenar_y_mostrar(lista):
    lista.sort()
    for i in lista:
        print(i)

# Devolvemos la longitud de la lista
def longitud_lista(lista):
    print(len(lista))

# Buscamos un elemento en la lista
def buscar_lista(lista, elemento):
    if elemento in lista:
        print(f"El elemento {elemento} se encuentra en la lista.")
    else:
        print(f"El elemento {elemento} no se encuentra en la lista.")

# Empezamos el programa con un menú para cada una de las opciones
while True:
    print("Menu:")
    print("1. Recorrer la lista y mostrarla")
    print("2. Devolver la lista como un string")
    print("3. Ordenar la lista y mostrarla")
    print("4. Mostrar la longitud de la lista")
    print("5. Buscar un elemento en la lista")
    print("6. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        mostrar_lista(lista)
    elif opcion == "2":
        lista_como_string = string_lista(lista)
        print(lista_como_string)
    elif opcion == "3":
        ordenar_y_mostrar(lista)
    elif opcion == "4":
        longitud_lista(lista)
    elif opcion == "5":
        elemento_a_buscar = int(input("Introduce el elemento a buscar: "))
        buscar_lista(lista, elemento_a_buscar)
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
