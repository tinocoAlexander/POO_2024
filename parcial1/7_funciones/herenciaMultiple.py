# Definición de la clase base Animal
class Animal:
    def respirar(self):
        print("Respirando")  # Método de la clase Animal

# Definición de la clase base Volador
class Volador:
    def volar(self):
        print("Volando")  # Método de la clase Volador

# Definición de la clase derivada Murcielago que hereda de Animal y Volador
class Murcielago(Animal, Volador):
    pass  # La clase Murcielago hereda métodos de Animal y Volador

# Creación de un objeto de la clase Murcielago
m = Murcielago()
m.respirar()  # Llamada al método heredado de la clase Animal
m.volar()  # Llamada al método heredado de la clase Volador
