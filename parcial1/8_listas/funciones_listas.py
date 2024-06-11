paises = ["Mexico", "USA", "Brasil", "Japón"]
numeros = [23,32,12.56,0.100]
texto = ["Hola", "True", 23, 3.141516]

#Ordenar una lista
print (paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

print(texto)
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto),True)
print(texto)

#Eliminar elementos
print(numeros)
numeros.pop(8)
print (numeros)

#Voltear elementos
numeros.reverse()
print (numeros)

#Buscar un dato dentro de una lista
respuesta = "Brasil" in paises
print(respuesta)

#Unir listas
print (paises)
paises.extend(numeros)
print (paises)