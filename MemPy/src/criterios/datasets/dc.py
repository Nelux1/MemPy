"""Contiene los métodos de obtención de datos del dataset de DC."""
import os
import csv


dc_path = os.path.join('resources', 'datasets', 'superheroes', 'dc-wikia-data.csv')


def obtener_nohumanos():
    """Obtiene los personajes no humanos."""
    with open(dc_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [personaje[1] for personaje in reader if not personaje[7]]


def obtener_muertos_ojos_rojos():
    """Obtiene los personajes fallecidos con ojos rojos."""
    with open(dc_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [
            personaje[1] for personaje in reader if personaje[5] == 'Red Eyes' 
            and personaje[-4] == 'Deceased Characters'
        ]


"""Variable que contiene todos los criterios posibles sobre los simpsons"""
criterios = {
    'criterio1': {
        'criterio': '125 personajes de DC no humanos', 
        'funcion': obtener_nohumanos, 
        'parametros': []
    },
    'criterio2': {
        'criterio': '60 personajes de DC fallecidos de ojos rojos', 
        'funcion': obtener_muertos_ojos_rojos, 
        'parametros': []
    }
}