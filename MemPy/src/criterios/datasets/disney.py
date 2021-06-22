"""Contiene los métodos de obtención de datos del dataset de disney."""
import os
import csv


disney_path = os.path.join('resources', 'datasets',
                           'disney', 'disney_movies.csv')


# Separa en una lista de diccionarios.
with open(disney_path, "r", encoding="utf-8") as archivo_disney:
    dicc_disney = []
    for i in csv.DictReader(archivo_disney):
        dicc_disney.append(dict(i))


# Funciones para encontrar los datos solicitados en el diccionario
def get_pelicula_con_genero_edad(genero, edad):
    data_juego = list(filter(lambda x: (
        x['genre'] == genero and x['mpaa_rating'] == edad), dicc_disney))
    return list(map(lambda nom: nom['movie_title'], data_juego))


def get_pelicula_con_dinero_genero(genero, dinero):
    data_juego = list(filter(lambda x: (x['genre'] == genero and int(
        x['total_gross']) >= dinero), dicc_disney))
    return list(map(lambda nom: nom['movie_title'], data_juego))


criterios = {
    'criterio1': {
        'criterio': 'Nombres de peliculas de Disney en genero musical para todas las edades',
        'funcion': get_pelicula_con_genero_edad,
        'parametros': ('Musical', 'G')
    },
    'criterio2': {
        'criterio': 'Nombres de peliculas de Disney en el genero de comedia, que produjeron mas de $70000000',
        'funcion': get_pelicula_con_dinero_genero,
        'parametros': ('Comedy', 70000000)
    },
    'criterio3': {
        'criterio': 'Nombres de peliculas de Disney en el genero de aventura, que produjeron mas de $100000000',
        'funcion': get_pelicula_con_dinero_genero,
        'parametros': ('Adventure', 100000000)
    },
    'criterio4': {
        'criterio': 'Nombres de peliculas de Disney en genero drama para mayores de 13',
        'funcion': get_pelicula_con_genero_edad,
        'parametros': ('Drama', 'PG-13')
    }
}

