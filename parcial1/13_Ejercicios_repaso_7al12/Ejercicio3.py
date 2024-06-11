lista = []
if not lista:
    print("No hay nada en la lista")
    while True:
        opcion=int(input("¿Quieres añadir una palabra? \n1)Si \n2)No\n"))
        if opcion==1:
            entrada = input("Introduce una palabra o frase: ")
            lista.append(entrada)
        else:
            break    

if lista:
    print("Contenido de la lista en mayúsculas:")
    for mayus in lista:
        print(mayus.upper())

