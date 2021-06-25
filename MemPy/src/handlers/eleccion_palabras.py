"""aca se van a ramdonizar las palabras de los criterios dependiendo las casillas del nivel"""
import random
import os

roja= os.path.join(
    'resources', 
    'icons', 
    'rojo.png'
)


def palabras(cant,palab):
 lista=[]
 p1= list(palab[1])
 lista= random.sample(p1,k=cant)
 lista2=lista
 lista.extend(lista2)
 return lista

def tablero (lista,event):
     l=''
     if event.startswith("pieza-") :         
         if event == 'pieza-0-0':
             l= lista[0] 
         elif event == 'pieza-0-1':
             l= lista[3]
         elif event == 'pieza-0-2':
             l= lista[4]
         elif event == 'pieza-0-3':
             l= lista[1]
         elif event == 'pieza-1-0':
             l= lista[2]
         elif event == 'pieza-1-1':
             l=lista[7]
         elif event == 'pieza-1-2':             
             l=lista[6]
         elif event == 'pieza-1-3':
             l=lista[5]
         elif event == 'pieza-2-0':
             l=lista[8]
         elif event == 'pieza-2-1':
             l=lista[11]
         elif event == 'pieza-2-2':
             l=lista[9]
         elif event == 'pieza-2-3':
             l=lista[10]
         elif event == 'pieza-3-0':
             l=lista[14]
         elif event == 'pieza-3-1':
             l=lista[12]
         elif event == 'pieza-3-2':
             l=lista[13]
         elif event == 'pieza-3-3':
             l=lista[15]                                                    
         return l

def play(player, window, event, board_data, toque):
    """
    Ejecuta una jugada sobre el tablero para un jugador:
    - Actualiza el tablero visual
    - Agrega el valor en board_data
    - Chequea si hay un ganador
    """
    window[event].update(player["value"],image_filename=roja)
    _prefix, x, y = event.split("-")
    board_data[int(x)][int(y)] = player["value"]
    if toque == 2:
     toque = 0

    return board_data


