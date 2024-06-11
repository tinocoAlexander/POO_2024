# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca  # Atributo de la clase Vehiculo

    def arrancar(self):
        print("El vehículo arranca")  # Método de la clase Vehiculo

# Definición de la clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo): # En java se utiliza la palabra extends
    def __init__(self, marca, numero_puertas):
        super().__init__(marca)  # Llamada al constructor de la clase base Vehiculo
        self.numero_puertas = numero_puertas  # Atributo específico de la clase Coche

    def tocar_claxon(self):
        print("El coche toca el claxon")  # Método específico de la clase Coche

# Creación de un objeto de la clase Coche
mi_coche = Coche("Toyota", 4)
mi_coche.arrancar()  # Llamada al método heredado de la clase Vehiculo
mi_coche.tocar_claxon()  # Llamada al método específico de la clase Coche
print(mi_coche.marca)
print(mi_coche.numero_puertas)
