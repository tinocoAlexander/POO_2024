# Definición de la clase base Animal
class Animal:
    def sonido(self):
        print("Sonido del animal")  # Método de la clase Animal

# Definición de la clase derivada Perro que hereda de Animal
class Perro(Animal):
    def sonido(self):
        print("Guau Guau")  # Método específico de la clase Perro

# Definición de la clase derivada Gato que hereda de Animal
class Gato(Animal):
    def sonido(self):
        print("Miau Miau")  # Método específico de la clase Gato

# Creación de objetos de las clases Perro y Gato
perro = Perro()
gato = Gato()
perro.sonido()  # Llamada al método específico de la clase Perro
gato.sonido()  # Llamada al método específico de la clase Gato
