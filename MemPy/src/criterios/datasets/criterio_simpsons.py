import csv
import os
from os import remove
import requests
import shutil
from PIL import Image

simpsons_path = os.path.join('resources', 'datasets', 'simpsons.csv')
simpsons_image= os.path.join('resources','datasets','images','imagenes_simpsons')

def temporada_1y2_mas_de_72000():
    """Retorna lista de imagenes de las temporadas 1 y 2 de mas de 72000 vistos"""
    imag=[]
    with open(simpsons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        episodios= filter(lambda x:x[4] >= '2'  and x[8] > '72000' , reader )
        for elem in episodios:
         try:
             Image.open(f'{simpsons_image}/You Only Move Twice_resize.png')   
             imag.append(f"{simpsons_image}/{elem[1]}_resize.png")
         except:
                response=requests.get(elem[11], stream=True)
                with open (f'{simpsons_image}/{elem[1]}.png','wb') as file:
                    shutil.copyfileobj(response.raw,file)
                del response
                imagen=Image.open(f'{simpsons_image}/{elem[1]}.png')
                imagen=imagen.resize((90,90))
                imagen.save(f"{simpsons_image}/{elem[1]}_resize.png")    
                imag.append(f"{simpsons_image}/{elem[1]}_resize.png")
                remove(f'{simpsons_image}/{elem[1]}.png')
                #remove(f'{simpsons_image}/{elem[0]}_resize.png')     
    return imag 

def todos_de_1994():
    """Retorna lista de imagenes de capitulos entre de 1994"""
    imag=[]
    with open(simpsons_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        episodios= filter(lambda x:x[2] >= '1994-01-01' and x[2] <= '1995-01-01', reader )
        for elem in episodios:
         try: 
             Image.open(f'{simpsons_image}/Shonen Ashibe GO! GO! Goma-chan_resize.png')   
             imag.append(f"{simpsons_image}/{elem[1]}_resize.png")
         except:
                response=requests.get(elem[11], stream=True)
                with open (f'{simpsons_image}/{elem[1]}.png','wb') as file:
                    shutil.copyfileobj(response.raw,file)
                del response
                imagen=Image.open(f'{simpsons_image}/{elem[1]}.png')
                imagen=imagen.resize((90,90))
                imagen.save(f"{simpsons_image}/{elem[1]}_resize.png")    
                imag.append(f"{simpsons_image}/{elem[1]}_resize.png")
                remove(f'{simpsons_image}/{elem[1]}.png')
                #remove(f'{simpsons_image}/{elem[1]}_resize.png')     
    return imag



criterios = {
    'criterio1': {
        'criterio': 'temporada_1 y 2  con mas de 72000 vistos',
        'funcion': temporada_1y2_mas_de_72000(),
    },
    'criterio2': {
        'criterio': 'capitulos de 1994',
       'funcion': todos_de_1994(),
   }
}

