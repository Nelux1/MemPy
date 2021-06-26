"""esta funcion se encarga de guardar todos los datos de la jugada en un archivo csv 
 y convierte en datasets"""

import csv
import os


archivo2=os.path.join(os.getcwd(),'posiciones.csv')
archivo=os.path.join(os.getcwd(),'datos_estadisticos.csv')


def guardando_data(nombre,edad,genero,tiempo,num_partida,nivel,palabras_adivinar,evento,estado,palabra,dia,hora):
    archivo_csv=open(archivo,"a")
    writer=csv.writer(archivo_csv)
    usuario=[nombre,edad,genero,tiempo,num_partida,nivel,palabras_adivinar,evento,estado,palabra,dia,hora]
    writer.writerow(usuario)
    archivo_csv.close() 
    return usuario

def puntos (username,puntaje):
  archivo_csv2=open(archivo2,"a")
  writer2=csv.writer(archivo_csv2)
  usuario=[username,puntaje]
  writer2.writerow(usuario)
  archivo_csv2.close()
  return usuario