"""posiciones se encarga de leer puntajes.json y hacer la comparacion con el usuario"""
import json
import os
import pandas as pd

arch_puntaje= os.path.join(os.getcwd(), 'default_puntajes.json')
dat= pd.read_json(arch_puntaje, orient='records')

def posiciones(username,puntaje):

 with open(arch_puntaje,'r',encoding='utf-8') as archivo_json:
     datos = json.load(archivo_json)
     with open(arch_puntaje,'w',encoding='utf-8') as archivo_json:
         datos+=[{'NOMBRE': username ,'PUNTAJE':puntaje,'PUESTO':10}]
         #lista_de_diccionarios = datos.append({'NOMBRE': username,'PUNTAJE':puntaje})
         lista_de_diccionarios= datos
         print(lista_de_diccionarios)
         json.dump(lista_de_diccionarios,archivo_json)
         datos = pd.DataFrame(lista_de_diccionarios)       
 return datos

