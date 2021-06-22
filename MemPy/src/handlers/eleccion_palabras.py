"""aca se van a ramdonizar las palabras de los criterios dependiendo las casillas del nivel"""
import random

def palabras(cant,palab):
 lista=[]
 p1= list(palab[1])
 lista= random.sample(p1,k=cant)
 lista2=lista
 lista.extend(lista2)

 return print(lista)