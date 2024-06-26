from clases import Rectangulos, Circulos

# Creación de objetos Rectangulos
rectangulo = Rectangulos(3,4,10,20,True)

# Creación de objetos Circulos
circulo= Circulos(3,3,6,True)


# Imprimir información de los objetos creados
print("Información del rectángulo:")
print(rectangulo.mostrar())
print(rectangulo.ocultar())

print("\nInformación del circulo:")
print(circulo.mostrar())
print(circulo.ocultar())



