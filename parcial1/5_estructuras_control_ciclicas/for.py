#Es un ciclo iterativo y se ejecuta x veces de acuerdo al rango de los valores numéricos enteros establecidos

#Sintaxis
"""""
for variable in elemento_iteriable(lista,rango,etc):
    bloque de instrucciones
"""""

#Ejemplo 1: crear un programa que imprimia 5 veces el carácter @

for i in range(1,6):
    print("@")

#Ejemplo 2: crear un programa que imprima los numeros del 1 al 5 los sume y al final imprimir la suma
print("------------------------------")
suma=0
for i in range(1,6):
    print(i)
    suma=suma+i
print(f"La suma es total a {suma}")    

#Ejemplo 3: crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente
print("Bienvenido a las tablas de multiplicar")
numero=int(input("Introduzca un numero para su tabla de multiplicar: "))
mult=0
for i in range(1,11):
    mult=numero*i 
    print(f"{numero} * {i} = {mult}")