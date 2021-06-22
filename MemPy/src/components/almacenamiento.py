"""esta funcion se encarga de guardar todos los datos de la jugada en un archivo csv 
 y convierte en datasets"""

import csv
import os

archivo=os.path.join(os.getcwd(),'datos_estadisticos.csv')
archivo_csv=open(archivo,"a")
data=csv.reader(archivo_csv,delimiter=',')
writer=csv.writer(archivo_csv)

def guardando_data(nombre,edad,genero,tiempo,num_partida,nivel,palabras_adivinar,evento,estado,palabra,dia_hora):   
    usuario=[nombre,edad,genero,tiempo,num_partida,nivel,palabras_adivinar,evento,estado,palabra,dia_hora]
    writer.writerow(usuario)
    archivo_csv.close() 
    return usuario

