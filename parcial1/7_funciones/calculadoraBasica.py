#Declaración de funciones para sumar, restar, multiplicar y dividir
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b


while True:
    print("Bienvenido a la calculadora básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    operacion = input("Por favor, elige una operación (1/2/3/4/5): ")
    if operacion in ['5']:
        break    
    if operacion in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Error: Por favor, introduce números válidos.")
        if operacion == '1':
            resultado = suma(num1, num2)
        elif operacion == '2':
            resultado = resta(num1, num2)
        elif operacion == '3':
            resultado = multiplicacion(num1, num2)
        elif operacion == '4':
            resultado = division(num1, num2)
        print(f"El resultado es: {resultado}")
    else:
        print("Operación no válida. Por favor, elige una operación del 1 al 4.")
    

