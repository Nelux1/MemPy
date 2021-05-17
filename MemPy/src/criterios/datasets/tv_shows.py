"""Contiene los métodos de obtención de datos del dataset de tv shows."""
import os
import csv


tv_shows_path = os.path.join('resources', 'datasets', 'tv_shows', 'TV_Shows.csv')


# Separa en una lista de diccionarios.
with open(tv_shows_path, "r", encoding="utf-8") as archivo_tv:
    dicc_tv = []
    for i in csv.DictReader(archivo_tv):
        dicc_tv.append(dict(i))


for r in dicc_tv:
    if r['IMDb'] == '':
        r['IMDb'] = '0'


# Funciones para encontrar los datos solicitados en el diccionario
def get_serie_con_netflix_IMDb_año(r_IMDb, año):
    data_juego = list(filter(lambda x: (
        x['Netflix'] == '1' and x['Year'] == año and float(x['IMDb']) >= r_IMDb), dicc_tv))
    return list(map(lambda nom: nom['Title'], data_juego))


def get_serie_con_Amazon_edad_año(edad, año):
    data_juego = list(filter(lambda x: (
        x['Prime Video'] == '1' and x['Year'] == año and x['Age'] == edad), dicc_tv))
    return list(map(lambda nom: nom['Title'], data_juego))


criterios = {
    'criterio1': {
        'criterio': 'Nombres de las series de Netflix, estrenadas en el año 2015 con nota de IMDb mayor a 8',
        'funcion': get_serie_con_netflix_IMDb_año,
        'parametros': (8, '2015')
    },
    'criterio2': {
        'criterio': 'Nombres de las series de Prime Video que se estrenaron en 2019 y son para mayores de 18 años',
        'funcion': get_serie_con_Amazon_edad_año,
        'parametros': ('18+', '2019')
    },
    'criterio3': {
        'criterio': 'Nombres de las series de Prime Video que se estrenaron en 2018 y son para mayores de 16 años',
        'funcion': get_serie_con_Amazon_edad_año,
        'parametros': ('16+', '2018')
    },
    'criterio4': {
        'criterio': 'Nombres de las series de Netflix, estrenadas en el año 2018 con nota de IMDb mayor a 7',
        'funcion': get_serie_con_netflix_IMDb_año,
        'parametros': (7, '2018')
    }
}
