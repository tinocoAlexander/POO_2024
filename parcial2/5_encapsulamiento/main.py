from coches import *

coche1 = Coche("VW", "Blanco", "2022", 220, 150, 5)
"""""
print("Este es el objeto 1")
# Crear una instancia de la clase Coche con valores iniciales


# Mostrar los valores iniciales del objeto o instancia de la clase
print(f"Los valores del coche son los siguientes:\n{coche1.get_info()}")

# Crear una segunda instancia de la clase Coche con diferentes valores
print("Este es el objeto 2")
coche2 = Coche("Nissan", "Azul", "2020", 180, 150, 6)

# Mostrar los valores iniciales del objeto o instancia de la clase
print(f"Los valores del coche son los siguientes:\n{coche2.get_info()}")

print("Este es el objeto 3")
# Crear una tercera instancia de la clase Coche y mostrar la información
coche3 = Coche("Lancer", "Azul Metálico", "2025", 240,300,6)
print(f"Los valores del coche son los siguientes:\n{coche3.get_info()}")
"""""

print(coche1.getPrivadoAtributo)