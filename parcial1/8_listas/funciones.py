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
