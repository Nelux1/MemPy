import csv
import os
from PIL import Image

pokemons_path = os.path.join('resources', 'datasets', 'pokemon.csv')
pokemons_image= os.path.join('resources','datasets','images','imagenes_pokemon')


def get_pokemons_fuego():
    """Retorna lista de los nombres de los pokemons de fuego"""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        fuego= filter(lambda x:x[1]== "Fire", reader )
        for elem in fuego:   
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag    
  

def get_pokemons_agua():
    """Retorna lista de los nombres de los pokemons de agua."""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        agua= filter(lambda x:x[1]== "Water", reader )
        for elem in agua:
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag

def get_pokemons_insecto():
    """Retorna lista de los nombres de los pokemons de insectos."""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        insecto= filter(lambda x:x[1]== "Bug", reader )
        for elem in insecto:
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag

def get_pokemons_normal():
    """Retorna lista de los nombres de los pokemons normales."""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        normal= filter(lambda x:x[1]== "Normal", reader )
        for elem in normal:
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag

def get_pokemons_peleador():
    """Retorna lista de los nombres de los pokemons peleadores"""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        peleador= filter(lambda x:x[1]== "Fighting", reader )
        for elem in peleador:
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag

def get_pokemons_psiquico():
    """Retorna lista de los nombres de los pokemons psiquicos"""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        psiquico= filter(lambda x:x[1]== "Psychic", reader )
        for elem in psiquico:
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag

def get_pokemons_electrico():
    """Retorna lista de los nombres de los pokemons electricos"""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        electrico= filter(lambda x:x[1]== "Electric", reader )
        for elem in electrico:
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag

def get_pokemons_roca():
    """Retorna lista de los nombres de los pokemons rocas"""
    imag=[]
    with open(pokemons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        roca= filter(lambda x:x[1]== "Rock", reader )
        for elem in roca:   
         imagen= Image.open(f"{pokemons_image}/{elem[0]}.png")
         imagen=imagen.resize((90,90))
         imagen.save(f"{pokemons_image}/{elem[0]}_resize.png")
         imag.append(f"{pokemons_image}/{elem[0]}_resize.png")     
    return imag     

criterios = {
    'criterio1': {
        'criterio': 'pokemons de fuego',
        'funcion': get_pokemons_fuego(),
    },
    'criterio2': {
        'criterio': 'pokemons de agua',
        'funcion': get_pokemons_agua(),
    },
    'criterio3': {
        'criterio': 'pokemons electricos',
        'funcion': get_pokemons_electrico(),
    },
    'criterio4': {
        'criterio': 'pokemons insectos',
        'funcion': get_pokemons_insecto(),
    },
    'criterio5': {
        'criterio': 'pokemons insectos',
        'funcion': get_pokemons_normal(),
    },
    'criterio6': {
        'criterio': 'pokemons insectos',
        'funcion': get_pokemons_psiquico()
    }
}
