"""posiciones se encarga de leer puntajes.json y hacer la comparacion con el usuario"""

import json
import os

archivo = os.path.join(os.getcwd(), 'default_puntajes.json')

def positions():
 lista=[]   
 with open(file= archivo, mode='r', encoding='utf-8') as f:
     try:
         with open(archivo, 'r') as f:
             data=json.load(f)
             for d in data:        
                 lista.append(d['-NOMBRE-'])
                 lista.append(d['-PUNTAJE-'])
                 lista.append(d['-PUESTO-'])            
     except:
         pass 
 
 return lista

print(positions())