from src.criterios.criterios import Criterios
import random


def pasando_lista(cant):
    dia_hora = Criterios.dia_semana_y_hora()
    lista = Criterios.seleccion_en(*dia_hora)
    lista_reducida = random.sample(lista[1], k=cant)
    lista_dup = lista_reducida
    lista_reducida.extend(lista_dup)
    return lista_dup

def armando_coordenadas (x,y):
    lista_coordenadas = []
    for i in range (0,x):
        for j in range(0,y):
            lista_coordenadas.append(tuple((i,j)))
    return lista_coordenadas

def diccionario_coordenadas(coordenadas, palabras):
    diccionario = {}
    for valor in coordenadas:
        palabra = random.choice(palabras)
        diccionario[valor]= palabra
        palabras.remove(palabra)
    return diccionario


print(pasando_lista(4))
print(armando_coordenadas(4,2))
coordenada = armando_coordenadas(4,2)
lista = pasando_lista(4)
print(diccionario_coordenadas(coordenada, lista))