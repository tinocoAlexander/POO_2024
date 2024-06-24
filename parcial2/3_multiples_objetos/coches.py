"""
Programación Orientada a Objetos (POO) o OOP

Clases: es como un molde a través del cual se puede instanciar un objeto. Dentro de las clases se 
definen atributos (propiedades/características) y los métodos (funciones o acciones).

Objetos o instancias: son parte de una clase, los objetos o instancias pertenecen a una clase.
Es decir, interactúan con la clase o clases y para hacer uso de los atributos y métodos es necesario
crear un objeto u objetos.
"""

"""
Ejemplo 1: crear una clase (un molde para crear más objetos) llamada Coche y a partir de la clase
crear objetos o instancias (coche) con características similares.
"""

class Coche:
    """
    - Atributos o propiedades (variables)
    - Características del coche
    - Valores iniciales es posible declarar al principio de una clase
    """

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    # Métodos o acciones o funciones que hace el objeto

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_caballaje(self):
        return self.caballaje

    def set_caballaje(self, caballaje):
        self.caballaje = caballaje

    def get_plazas(self):
        return self.plazas

    def set_plazas(self, plazas):
        self.plazas = plazas

    def get_info(self):
        return f"Marca: {self.marca}, Color: {self.color}, Modelo: {self.modelo}, Velocidad: {self.velocidad}, Caballaje: {self.caballaje}, Plazas: {self.plazas}"

# Fin de definición de la clase

print("Este es el objeto 1")
# Crear una instancia de la clase Coche con valores iniciales
coche1 = Coche("Ferrari", "Rojo", "2010", 300, 500, 2)

# Mostrar los valores iniciales del objeto o instancia de la clase
print(f"Los valores del coche son los siguientes:\n{coche1.get_info()}")

# Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.get_velocidad()}")

# Disminuir la velocidad del coche de 301 a 100
for _ in range(201):  # El rango debe ser 201 para disminuir 201 unidades y llegar a 100
    coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.get_velocidad()}")

# Crear una segunda instancia de la clase Coche con diferentes valores
print("Este es el objeto 2")
coche2 = Coche("Honda", "Azul", "2012", 100, 300, 3)

# Mostrar los valores iniciales del objeto o instancia de la clase
print(f"Los valores del coche son los siguientes:\n{coche2.get_info()}")

print("Este es el objeto 3")
# Crear una tercera instancia de la clase Coche y mostrar la información
coche3 = Coche("Lancer", "Azul Metálico", "2014", 220, 300, 5)
print(f"Los valores del coche son los siguientes:\n{coche3.get_info()}")
