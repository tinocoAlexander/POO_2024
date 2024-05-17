"""
    Existe una estructura de condición llamada "If"
    La cual evalua una condición para encontrar el valor "True" o se cumple
    la condición se ejecuta la linea o lineas de codigo

    Tiene 4 variantes

    1. If simple
    2. If compuesto
    3. If anidado
    4. If y elif
"""

#Ejemplo 1: If simple
color="rojo"
if(color=="rojo"):
    print("Soy rojo")

#Ejemplo 2: If compuesto
if(color=="rojo"):
    print("Soy rojo")
else:
    print("No soy rojo")  

#Ejemplo 3: If anidado
if(color=="rojo"):
    print("Soy rojo")
    if(color!="rojo"):
        print("Soy otro color")
else:
    print("No soy el color rojo")
    if (color!="rojo"):
        print("Soy otro color")

#Ejemplo 4: If con el elif
if(color=="rojo"):
    print("Soy color rojo")
elif(color=="negro"):
    print("Soy color negro")
elif(color=="verde"):
    print("Soy color verde")                