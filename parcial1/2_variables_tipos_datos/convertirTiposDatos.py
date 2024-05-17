#Nota: cuando se imprime en pantalla una cadena de caracteres
#se trabaja por default con "cadenas", es decir python no
#puede concatenar otra cosa que no sea un String[str]

texto="Soy una cadena de caracteres"
numero=23

#concatenar str con str
print("Soy otra cadena y "+texto)

#concatenar str con int
print("El numero es: "+str(numero))

#imprimir caracteres especiales
print("el numero: "+"\""+str(numero)+"\"")

#concatenar un int con str
n1="23"
n2="33"
suma=int(n1)+int(n2)
print("La suma es: "+str(suma))

#otra forma de imprimir o concatenar
print("La suma es ",suma)

#concatenar float e int con str
n1=23
n2=42.5
suma=n1+n2
print(f"La suma es: {suma}")