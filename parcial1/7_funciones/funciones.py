"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1.- Funcion que no recibe parametros y no regresa valor
   2.- Funcion que no recibe parametros y regresa valor
   3.- Funcion que recibe parametros y no regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas
#    1.- Funcion que no recibe parametros y no regresa valor 
def solicitarNombres():
   nombre=input("Ingresa el nombre completo: ")

solicitarNombres()  

#Ejemplo 2 sumar dos numeros
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()    

#Ejemplo 3 sumar dos numeros 
#2.- Funcion que no recibe parametros y regresa valor
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejemplo 4 sumar dos numeros 
# 3.- Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5 sumar dos numeros 
# 4.- Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")

#Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del Paciente, Edad, Estatura, Tipo de Sangre. Utilizar los 4 tipos de funciones
def solicitarNombre():
    global nombre
    nombre = input("Ingresa el nombre completo del paciente: ")

def obtenerEdad():
    edad = int(input("Ingresa la edad del paciente: "))
    return edad

def mostrarEstaturaYTipoSangre(estatura, tipo_sangre):
    print(f"La estatura del paciente es: {estatura} metros")
    print(f"El tipo de sangre del paciente es: {tipo_sangre}")

def formatearInformacion(nombre, edad):
    return f"Nombre del paciente: {nombre}, Edad: {edad} años"

# 1. Solicitar el nombre del paciente
solicitarNombre()

# 2. Obtener la edad del paciente
edad_paciente = obtenerEdad()

# 3. Solicitar estatura y tipo de sangre, y luego mostrar estos valores
estatura_paciente = float(input("Ingresa la estatura del paciente en metros: "))
tipo_sangre_paciente = input("Ingresa el tipo de sangre del paciente: ")
mostrarEstaturaYTipoSangre(estatura_paciente, tipo_sangre_paciente)

# 4. Formatear y mostrar la información del paciente con nombre y edad
info_paciente = formatearInformacion(nombre, edad_paciente)
print(info_paciente)





