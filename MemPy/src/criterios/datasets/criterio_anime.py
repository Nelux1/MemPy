import csv
import os
from os import remove
import requests
import shutil
from PIL import Image

animes_path = os.path.join('resources', 'datasets', 'animes.csv')
animes_image= os.path.join('resources','datasets','images','imagenes_anime')

def costo_de_0_a_2_aventura():
    """Retorna lista de imagenes de series anime 
    donde el costo de crunchyroll es entre 0 a 2 dolares"""
    imag=[]
    with open(animes_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        episodios= filter(lambda x:x[6] > '0' and x[6] < '2.0' and x[13], reader )
        for elem in episodios:
         try:
             Image.open(f'{animes_image}/Izumo: Flash of a Brave Sword_resize.png')   
             imag.append(f"{animes_image}/{elem[0]}_resize.png")
         except:
                response=requests.get(elem[2], stream=True)
                with open (f'{animes_image}/{elem[0]}.png','wb') as file:
                    shutil.copyfileobj(response.raw,file)
                del response
                imagen=Image.open(f'{animes_image}/{elem[0]}.png')
                imagen=imagen.resize((90,90))
                imagen.save(f"{animes_image}/{elem[0]}_resize.png")    
                imag.append(f"{animes_image}/{elem[0]}_resize.png")
                remove(f'{animes_image}/{elem[0]}.png')
                #remove(f'{animes_image}/{elem[0]}_resize.png')     
    return imag 

def mas_de_80000_votos_comedia():
    """Retorna lista de de imagenes de animes con mas de 80000 votos"""
    imag=[]
    with open(animes_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        episodios= filter(lambda x:x[4] > '80000' and x[14] >= '1', reader )
        for elem in episodios:
         try: 
             Image.open(f'{animes_image}/Shonen Ashibe GO! GO! Goma-chan_resize.png')   
             imag.append(f"{animes_image}/{elem[0]}_resize.png")
         except:
                response=requests.get(elem[2], stream=True)
                with open (f'{animes_image}/{elem[0]}.png','wb') as file:
                    shutil.copyfileobj(response.raw,file)
                del response
                imagen=Image.open(f'{animes_image}/{elem[0]}.png')
                imagen=imagen.resize((90,90))
                imagen.save(f"{animes_image}/{elem[0]}_resize.png")    
                imag.append(f"{animes_image}/{elem[0]}_resize.png")
                remove(f'{animes_image}/{elem[0]}.png')
                #remove(f'{animes_image}/{elem[0]}_resize.png')     
    return imag

def mas_de_500_episodios_accion():
    """Retorna lista de animes de accion con mas de 500 episodios"""
    imag=[]
    with open(animes_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        episodios= filter(lambda x:x[3] >= '500' and x[12] >= '1', reader )
        for elem in episodios:
         try: 
             Image.open(f'{animes_image}/Squishy! Black Clover_resize.png') 
             imag.append(f"{animes_image}/{elem[0]}_resize.png")
         except:
                response=requests.get(elem[2], stream=True)
                with open (f'{animes_image}/{elem[0]}.png','wb') as file:
                    shutil.copyfileobj(response.raw,file)
                del response
                imagen=Image.open(f'{animes_image}/{elem[0]}.png')
                imagen=imagen.resize((90,90))
                imagen.save(f"{animes_image}/{elem[0]}_resize.png")    
                imag.append(f"{animes_image}/{elem[0]}_resize.png")
                remove(f'{animes_image}/{elem[0]}.png')
                #remove(f'{animes_image}/{elem[0]}_resize.png')     
    return imag

criterios = {
    'criterio1': {
        'criterio': 'mas_de_500_episodios_accion',
        'funcion': mas_de_500_episodios_accion(),
    },
    'criterio2': {
        'criterio': 'mas_de_80000_votos_comedia',
        'funcion': mas_de_80000_votos_comedia(),
    },
    'criterio3': {
        'criterio': 'costo_de_0_a_2_aventura',
        'funcion': costo_de_0_a_2_aventura(),
    }, 
}
