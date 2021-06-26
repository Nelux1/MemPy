"""esta funcion se encarga de guardar todos los datos de la jugada en un archivo csv 
 y convierte en datasets"""

import csv
import os


archivo2=os.path.join(os.getcwd(),'posiciones.csv')
archivo_csv2=open(archivo2,"a")
writer2=csv.writer(archivo_csv2)

archivo=os.path.join(os.getcwd(),'datos_estadisticos.csv')
archivo_csv=open(archivo,"a")
data=csv.reader(archivo_csv,delimiter=',')
writer=csv.writer(archivo_csv)

def guardando_data(nombre,edad,genero,tiempo,num_partida,nivel,palabras_adivinar,evento,estado,palabra,dia,hora):   
    usuario=[nombre,edad,genero,tiempo,num_partida,nivel,palabras_adivinar,evento,estado,palabra,dia,hora]
    writer.writerow(usuario)
    archivo_csv.close() 
    return usuario

def puntos (username,puntaje):
  usuario=[username,puntaje]
  writer2.writerow(usuario)
  archivo_csv2.close()
  return usuario