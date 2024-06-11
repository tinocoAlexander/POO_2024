def tipo_impresión(variable):
    if type(variable) == list:
        print ("La variables es una lista")
    elif type(variable) == str:
        print ("La variables es una cadena")
    elif type(variable) == int:
        print ("La variables es un entero")
    elif type(variable) == bool:
        print ("La variables es un boleano")
    else:
        print ("La variables es de otro tipo")


# Declaración de variables
lista = [1, 2, 3, 4, 5]
cadena = "Alexander"
entero = 777
boleano = True

# Llamada a las funciones para imprimir el mensaje según el tipo de dato
tipo_impresión(lista)
tipo_impresión(cadena)
tipo_impresión(entero)
tipo_impresión(boleano)
