import pandas as pd
import os
import json

arch_puntaje= os.path.join(os.getcwd(), 'default_puntajes.json')
dat= pd.read_json(arch_puntaje, orient='records')

def posiciones(username,puntaje):

 with open(arch_puntaje,'r',encoding='utf-8') as archivo_json:
     datos = json.load(archivo_json)
     with open(arch_puntaje,'w',encoding='utf-8') as archivo_json:
         datos+=[{'NOMBRE': username,'PUNTAJE':puntaje,'PUESTO':10}]
         #lista_de_diccionarios = datos.append({'NOMBRE': username,'PUNTAJE':puntaje})
         lista_de_diccionarios= datos
         print(lista_de_diccionarios)
         json.dump(lista_de_diccionarios,archivo_json)
         datos = pd.DataFrame(lista_de_diccionarios)
    
 return datos 

def positions():
 lista=[]   
 with open(file= arch_puntaje, mode='r', encoding='utf-8') as f:
     try:
         with open(arch_puntaje, 'r') as f:
             data=json.load(f)
             for d in data:        
                 lista.append(d['-NOMBRE-'])
                 lista.append(d['-PUNTAJE-'])
                 lista.append(d['-PUESTO-'])            
     except:
         pass 
 
 return lista

positions() 