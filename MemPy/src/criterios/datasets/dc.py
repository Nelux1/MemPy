"""Contiene los métodos de obtención de datos del dataset de DC."""
import os
import csv


dc_path = os.path.join('resources', 'datasets', 'superheroes', 'dc-wikia-data.csv')


def obtener_personaje_pelo_vivo(pelo, vivo):
    """Personajes de dc con pelo negro y que estan vivos"""
    with open(dc_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [personaje[1] for personaje in reader if personaje[6] == pelo
               and personaje[9] == vivo]


def obtener_muertos_ojos_rojos(ojos,vivo):
    """Obtiene los personajes fallecidos con ojos rojos."""
    with open(dc_path, encoding='utf-8') as f:
        reader = csv.reader(f)

        return [
            personaje[1] for personaje in reader if personaje[5] == ojos 
            and personaje[9] == vivo
        ]


"""Variable que contiene todos los criterios posibles sobre los personajes de dc"""
criterios = {
    'criterio1': {
        'criterio': 'Personajes de dc con pelo negro y que estan vivos', 
        'funcion': obtener_personaje_pelo_vivo, 
        'parametros': ('Black Hair', 'Living Characters')
    },
    'criterio2': {
        'criterio': 'personajes de dc que estan muertos con ojos rojos', 
        'funcion': obtener_muertos_ojos_rojos, 
        'parametros': ('Red Eyes','Deceased Characters')
    }
}
