"""Contiene los métodos de obtención de datos del dataset de marvel."""
import os
import csv


marvel_path = os.path.join('resources', 'datasets', 'superheroes', 'marvel-wikia-data.csv')


def obtener_villanas(sexo, id, alineacion,ojos):
    """Obtiene las villanas de identidad secreta y ojos azules."""
    with open(marvel_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [
            personaje[1] for personaje in reader if personaje[7] == sexo 
            and personaje[3] == id
            and personaje[4] == alineacion
            and personaje [5] == ojos
        ]


def obtener_calvas(sexo, pelo):
    """Obtiene los personajes femeninos calvos."""
    with open(marvel_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [
            personaje[1] for personaje in reader if personaje[7] == sexo 
            and personaje[6] in pelo
        ]


"""Variable que contiene todos los criterios posibles sobre los personajes de marvel"""
criterios = {
    'criterio1': {
        'criterio': 'Obtiene las villanas de identidad secreta y ojos azules', 
        'funcion': obtener_villanas, 
        'parametros': ('Female Characters','Secret Identity','Bad Characters','Blue Eyes')
    },
    'criterio2': {
        'criterio': 'Obtiene los personajes femeninos calvos', 
        'funcion':  obtener_calvas,
        'parametros': ('Female Characters','Bald')
    }
}

