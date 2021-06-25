"""Contiene los métodos de obtención de datos del dataset de steam."""
import os
import csv


steam_path = os.path.join('resources', 'datasets', 'steam', 'steam.csv')


# Separa en una lista de diccionarios.
with open(steam_path, "r", encoding="utf-8") as archivo_steam:
    dicc_steam = []
    for i in csv.DictReader(archivo_steam):
        dicc_steam.append(dict(i))


# Funciones para encontrar los datos solicitados en el diccionario
def get_juego_con_publisher_developer(publicador, desarrollador):
    data_juego = list(filter(lambda x: (
        x['publisher'] == publicador and x['developer'] == desarrollador), dicc_steam))
    return list(map(lambda nom: nom['name'], data_juego))


def get_developer_con_genero_precio_positivos(genero, precio, positivos):
    data_juego = list(filter(lambda x: (x['genres'] == genero and float(
        x['price']) <= precio and int(x['positive_ratings']) >= positivos), dicc_steam))
    return set(list(map(lambda nom: nom['developer'], data_juego)))


criterios = {
    'criterio1': {
        'criterio': 'Nombres de juegos desarrollados y publicados por Valve',
        'funcion': get_juego_con_publisher_developer,
        'parametros': ('Valve', 'Valve')
    },
    'criterio2': {
        'criterio': 'Nombres de desarrolladoras con juegos del genero de accion, menores a $10 de precio, y mas de 1000 positivos',
        'funcion': get_developer_con_genero_precio_positivos,
        'parametros': ('Action', 10, 1000)
    },
    'criterio3': {
        'criterio': 'Nombres de desarrolladoras con juegos del genero RPG menores a $30 de precio, y mas de 5000 positivos',
        'funcion': get_developer_con_genero_precio_positivos,
        'parametros': ('RPG', 30, 5000)
    },
    'criterio4': {
        'criterio': 'Nombres de juegos desarrollados por Bethesda Game Studios y publicados por Bethesda Softworks',
        'funcion': get_juego_con_publisher_developer,
        'parametros': ('Bethesda Softworks', 'Bethesda Game Studios')
    }
}

