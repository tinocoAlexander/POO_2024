"""""
    El ciclo while es una estructura de control que itera o repite la ejecución de una serie de instrucciones
    tantas veces como la condición se cumpla "True"
"""""

#Sintaxis
"""""
    While condicion:
        bloque instrucciones
"""""
#Ejemplo 1: crear un programa que imprimia 5 veces el carácter @
i=1
while i<=5:
    print("@")
    i+=1

#Ejemplo 2: crear un programa que imprima los numeros del 1 al 5 los sume y al final imprimir la suma
print("-----------------")
i=1
suma=0
while i<=5:
    print(i)
    suma+=i
    i+=1
print(f"La suma total es {suma}")    

#Ejemplo 3: crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente
print("Bienvenido a las tablas de multiplicar")
numero=int(input("Ingrese un numero para sacar su tabla de multiplicar"))
i=1
mult=0
while i<=10:
    mult=numero*i
    print(f"{numero} * {i} = {mult}")
    i+=1