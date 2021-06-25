"""Contiene los métodos de obtención de datos del dataset de pokemon."""
import os
import csv


pokemons_path = os.path.join('resources', 'datasets', 'pokemon', 'pokemon.csv')


def get_pokemons_legendarios(legendario,poder):
    """Retorna lista de los nombres de los pokemons legendarios con velocidad mayor a la estipulada."""
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        return [pokemon[-11] for pokemon in reader if pokemon[-1] == legendario and pokemon[-6] >= poder]
        

def get_pokemons_nolegendarios_detipo(legendario,tipo):
    """Retorna lista de los nombres de pokemons tipo agua, no legendarios"""
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        return [pokemon[-11] for pokemon in reader if pokemon[-1] == legendario and pokemon[-5] == tipo]

"""Variable que contiene todos los criterios posibles sobre pokemons"""
criterios = {
    'criterio1': {
        'criterio': 'Retorna lista de los nombres de los pokemons legendarios', 
        'funcion': get_pokemons_legendarios, 
        'parametros': ('1','2')
    },
    'criterio2': {
        'criterio': 'Retorna lista de los nombres de pokemons tipo agua, no legendarios',
        'funcion': get_pokemons_nolegendarios_detipo, 
        'parametros': ('0','water')
    },
    'criterio3': {
        'criterio': 'Retorna lista de los nombres de pokemons tipo planta, no legendarios',
        'funcion': get_pokemons_nolegendarios_detipo, 
        'parametros': ('0','grass')
    }
}
