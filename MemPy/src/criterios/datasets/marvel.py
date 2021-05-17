"""Contiene los métodos de obtención de datos del dataset de marvel."""
import os
import csv


marvel_path = os.path.join('resources', 'datasets', 'superheroes', 'marvel-wikia-data.csv')


def obtener_villanas():
    """Obtiene las villanas de identidad secreta y ojos azules."""
    with open(marvel_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [
            personaje[1] for personaje in reader if personaje[7] == 'Female Characters' 
            and personaje[3] == 'Secret Identity' 
            and personaje[4] == 'Bad Characters' 
            and personaje [5] == 'Blue Eyes'
        ]


def obtener_calvas():
    """Obtiene los personajes femeninos calvos."""
    with open(marvel_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [
            personaje[1] for personaje in reader if personaje[7] == 'Female Characters' 
            and personaje[6] in ('Bald', 'No Hair')
        ]


"""Variable que contiene todos los criterios posibles sobre los simpsons"""
criterios = {
    'criterio1': {
        'criterio': '81 villanas de marvel con identidad secreta y ojos azules', 
        'funcion': obtener_villanas, 
        'parametros': []
    },
    'criterio2': {
        'criterio': '135 personajes de marvel femeninos, calvos.', 
        'funcion':  obtener_calvas,
        'parametros': []
    }
}


