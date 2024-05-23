alumnos = []
numero_alumno=1
while True:
    nombre = input("Nombre del alumno: ")
    carrera = input("Carrera: ")
    suma_parcial=0
    for i in range(1, 4):
        while True:
            try:
                parcial = float(input(f"Calificación del parcial {i} para el alumno {numero_alumno}: "))
                suma_parcial+=parcial
                break
            except ValueError:
                print("Error, la calificación del parcial tiene que ser un numero")
    #-------------------------            
    promedio_parciales=suma_parcial/3
    #-------------------------    
    while True:
        try:
            proyecto_final = float(input("Calificación del proyecto final: "))
            break
        except ValueError:
            print("Error, la calificación del proyecto final tiene que ser un numero")
    calificacion_final = promedio_parciales/2 + proyecto_final/2
    
    print("-----------------")
    print(f"Nombre: {nombre}")
    print(f"Carrera: {carrera}")
    print(f"Promedio de parciales: {promedio_parciales}")
    print(f"Calificación proyecto final: {proyecto_final}")
    print(f"Calificación final: {calificacion_final}")
    if calificacion_final < 80 and proyecto_final > 50:
        print("Presenta examen extraordinario")
    print("-----------------")
    
    alumnos.append(calificacion_final)

    pregunta = input("\n¿Deseas otra captura? (Si/No): ").strip()
    if pregunta == "NO" or pregunta=="No" or pregunta=="no" or pregunta == "nO":
        break
    else:
        numero_alumno+=1

promedio_final = sum(alumnos) / len(alumnos)
print("---------------------")
print(f"Promedio de la calificación final de todos los alumnos capturados: {promedio_final}") 
print("---------------------")   
