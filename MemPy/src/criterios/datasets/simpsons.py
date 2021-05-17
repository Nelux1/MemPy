"""Contiene los métodos de obtención de imagenes de los simpsons."""
import os
import random


simpsons_path = os.path.join('resources', 'datasets', 'simpsons')


def obtener_imgs_de(nombre):
    """Retorna 50 imagenes random del nombre dado.
    
        Nombres posibles son:
            homer, bart, marge

        La selección se hace entre 500 imágenes.
    """
    path = os.path.join(simpsons_path, f'{nombre}_simpson')
    return [
        os.path.join(path, f'pic_{str(i).zfill(4)}.jpg') 
        for i in random.sample(range(0, 500), k=50)
    ]


"""Variable que contiene todos los criterios posibles sobre los simpsons"""
criterios = {
    'criterio1': {
        'criterio': '50 imagenes random de Homero Simpson', 
        'funcion': obtener_imgs_de, 
        'parametros': ['homer']
    },
    'criterio2': {
        'criterio': '50 imagenes random de Marge Simpson', 
        'funcion': obtener_imgs_de, 
        'parametros': ['marge']
    },
    'criterio3': {
        'criterio': '50 imagenes random de Bart Simpson', 
        'funcion': obtener_imgs_de, 
        'parametros': ['bart']
    }
}