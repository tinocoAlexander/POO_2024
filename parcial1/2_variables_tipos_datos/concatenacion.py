#Formas de concatenación en Python

nombre="Alexander Tinoco"
especialidad="Area de SW multiplataforma"
carrera="Ingeniería en Gestión y Desarrollo de SW"

#1er forma
print("Mi nombre es "+nombre+" estoy en la especialidad de "+especialidad+" en la carrera de "+carrera)
print("\n")

#2na forma
print("Mi nombre es ",nombre," estoy en la especialidad de ",especialidad," en la carrera de ",carrera)
print("\n")

#3ra forma
print(f"Mi nombre es {nombre} y estoy en la especialidad de {especialidad} en la carrera de {carrera}")
print("\n")

#4ta forma
print("Mi nombre es {} y estoy en la especialidad de {} en la carrera de {}".format(nombre,especialidad,carrera))
print("\n")

#5ta forma
print('Mi nombre es '+nombre+' estoy en la especialidad de '+especialidad+' en la carrera de '+carrera)
print("\n")