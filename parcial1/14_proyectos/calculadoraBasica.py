import math


    

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(a)


while True:
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")
    opcion = input("Ingrese la opción (1/2/3/4/5/6): ")
    if opcion in ['7']:
        print("Bye bye")
        break
    if opcion in ['1', '2', '3', '4', '5']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    if opcion == '1':
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {restar(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {dividir(num1, num2)}")
    elif opcion == '5':
        print(f"Resultado: {potencia(num1, num2)}")
    elif opcion == '6':
        num = float(input("Ingrese el número: "))
        print(f"Resultado: {raiz_cuadrada(num)}")
    else:
        print("Opción no válida. Intente de nuevo.")
        
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break

