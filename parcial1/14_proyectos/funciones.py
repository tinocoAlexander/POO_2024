def agregar_pelicula(lista_peliculas, pelicula):
    lista_peliculas.append(pelicula)
    print(f"La película '{pelicula}' ha sido agregada a la lista.")

def remover_pelicula(lista_peliculas, pelicula):
    if pelicula in lista_peliculas:
        lista_peliculas.remove(pelicula)
        print(f"La película '{pelicula}' ha sido removida de la lista.")
    else:
        print(f"La película '{pelicula}' no se encontró en la lista.")

def consultar_peliculas(lista_peliculas):
    if lista_peliculas:
        print("Lista de películas:")
        for i, pelicula in enumerate(lista_peliculas, start=1):
            print(f"{i}. {pelicula}")
    else:
        print("No hay películas en la lista.")

def actualizar_pelicula(lista_peliculas, nombre_viejo, nombre_nuevo):
    if nombre_viejo in lista_peliculas:
        indice = lista_peliculas.index(nombre_viejo)
        lista_peliculas[indice] = nombre_nuevo
        print(f"La película '{nombre_viejo}' ha sido actualizada a '{nombre_nuevo}'.")
    else:
        print(f"La película '{nombre_viejo}' no se encontró en la lista.")

def buscar_pelicula(lista_peliculas, nombre):
    if nombre in lista_peliculas:
        print(f"La película '{nombre}' está en la lista.")
    else:
        print(f"La película '{nombre}' no se encontró en la lista.")

def vaciar_lista(lista_peliculas):
    lista_peliculas.clear()
    print("La lista de películas ha sido vaciada.")
