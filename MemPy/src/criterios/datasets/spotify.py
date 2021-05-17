"""Contiene los métodos de obtencion de datos del dataset de steam."""
import os
import csv


spotify_path = os.path.join('resources', 'datasets',
                            'spotify', 'Spotify-2000.csv')


# Separa en una lista de diccionarios.
with open(spotify_path, "r", encoding="utf-8") as archivo_musica:
    dicc_musica = []
    for i in csv.DictReader(archivo_musica):
        dicc_musica.append(dict(i))


# Funciones para encontrar los datos solicitados en el diccionario
def get_cancion_con_artista_año(artista, años):
    data_juego = list(filter(lambda x: (
        x['Artist'] == artista and int(x['Year']) in años), dicc_musica))
    return list(map(lambda nom: nom['Title'], data_juego))


def get_artista_con_genero_año_popularidad(genero, años, popularidad):
    data_juego = list(filter(lambda x: (x['Top Genre'] == genero and int(
        x['Year']) in años and int(x['Popularity']) >= popularidad), dicc_musica))
    return list(set(map(lambda nom: nom['Artist'], data_juego)))


criterios = {
    'criterio1': {
        'criterio': 'Nombres de las canciones mas populares de Coldplay del año de 2000 hasta 2009',
        'funcion': get_cancion_con_artista_año,
        'parametros': ('Coldplay', list(range(2000, 2010, 1)))
    },
    'criterio2': {
        'criterio': 'Nombres de los artistas con popularidad mayor o igual a 30 en la categoria de dance pop, en los años de 2010 hasta 2019',
        'funcion': get_artista_con_genero_año_popularidad,
        'parametros': ('dance pop', list(range(2010, 2020, 1)), 30)
    },
    'criterio3': {
        'criterio': 'Nombres de los artistas con popularidad mayor a 40 en la categoria de album rock, en los años de 2000 hasta 2014',
        'funcion': get_artista_con_genero_año_popularidad,
        'parametros': ('album rock', list(range(2000, 2015, 1)), 50)
    },
    'criterio4': {
        'criterio': 'Nombres de las canciones mas populares de los Rolling Stones del año 1969 hasta 1980',
        'funcion': get_cancion_con_artista_año,
        'parametros': ('The Rolling Stones', list(range(1969, 1981, 1)))
    }
}
