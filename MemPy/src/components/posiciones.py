"""posiciones se encarga de leer puntajes.json y hacer la comparacion con el usuario"""
import pandas as pd
import os
import csv
import pandas as pd


archivo=os.path.join(os.getcwd(),'posiciones.csv')
archivo_csv=open(archivo,"a")
writer=csv.writer(archivo_csv)

def posiciones(username,puntaje):
 usuario=[username,puntaje]
 df = pd.read_csv(archivo_csv, sep=',',encoding='utf-8')
 for x in df:
     if usuario[username] == x['NOMBRE']:
         pass
     else:      
         writer.writerow(usuario)       
  



