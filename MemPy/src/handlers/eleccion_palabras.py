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
 lista= lista.sort()
 return lista

def tablero (lista,cant,board_data):
    for x in range (4):
        for y in range (cant):
         if board_data[int(x)][int(y)] == 'pieza: 0,0':
             board_data= 'PROBANDO'
    return board_data

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


