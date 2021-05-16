"""Contiene los métodos de obtención de datos del dataset de pokemon."""
import os
import csv


pokemons_path = os.path.join('resources', 'datasets', 'pokemon', 'pokemon.csv')


def get_pokemons_legendarios():
    """Retorna lista de los nombres de los 53 pokemons legendarios.
    
        Evita los de generación 7 porque no tienen una imagen en PNG
        correspondiente :(
    """
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        return [pokemon[-11] for pokemon in reader if pokemon[-1] == '1' and pokemon[-2] != '7']
        

def get_pokemons_nolegendarios_detipo(tipo):
    """Retorna lista de los nombres de 100 pokemons de del tipo dado no legendarios.
    
        Evita los de generación 7 porque no tienen una imagen en PNG
        correspondiente :(
    """
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        return [pokemon[-11] for pokemon in reader if pokemon[-1] == '0' and pokemon[-5] == tipo and pokemon[-2] != '7']


def get_imagenes(pokemons):
    """Obtiene los paths de las imagenes de los pokemons dados.
    
        Parametros
        ---------
            pokemons : list[str]

        Return
        ------
            list(tuple()) : [(pokemon, path_imagen), ...]
    """
    path_imagenes = os.path.join('resources', 'datasets', 'pokemon', 'images')


    imagenes = []
    for pokemon in pokemons:
        imagenes.append(os.path.join(path_imagenes, pokemon.lower().replace(' ', '-') + '.png'))

    return list(zip(pokemons, imagenes))


"""Variable que contiene todos los criterios posibles sobre pokemons"""
criterios = {
    'criterio1': {
        'criterio': '53 pokemons legendarios entre generaciones 1 y 6', 
        'funcion': get_pokemons_legendarios, 
        'parametros': []
    },
    'criterio2': {
        'criterio': '100 pokemons no legendarios de agua entre generaciones 1 y 6',
        'funcion': get_pokemons_nolegendarios_detipo, 
        'parametros': ['water']
    },
    'criterio3': {
        'criterio': '64 pokemons no legendarios tipo planta entre generaciones 1 y 6',
        'funcion': get_pokemons_nolegendarios_detipo, 
        'parametros': ['grass']
    }
}