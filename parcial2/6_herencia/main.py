from coches import *

coche1 = Coche("VW", "Blanco", "2022", 220, 150, 5)

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

camion1=Camiones("Dina","Negro","2020",150,300,14,6,2000) 
camion1.get_info
camion2=Camiones("Star","Azul","2019",150,300,14,6,2000) 
camion2.get_info


camioneta1=Camionetas("Renault", "Amarillo", "2025", 240, 250, 8, "Delantera", True)
camioneta1.get_info
camioneta2=Camionetas("Nissan", "Blanco", "2020", 180, 150, 6, "Trasera", False)
camioneta2.get_info