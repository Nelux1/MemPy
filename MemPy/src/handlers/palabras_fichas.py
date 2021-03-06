"""aca se van a ramdonizar las palabras de los criterios dependiendo las casillas del nivel"""
import random
import os
import time as t
from src.windows import colors


image= os.path.join('resources','datasets','images')


cart= os.path.join(
    'resources', 
    'icons', 
    'oculta9.png'
)
acierto= os.path.join(
    'resources', 
    'icons', 
    'outline_close_black_48dp9.png'
)
pista=os.path.join(
    'resources',
    'icons',
    'lupa9.png'

)
roja= os.path.join(
    'resources', 
    'icons', 
    'rojo.png'
)


def palabras(cant,palab,img):
 lista=[]   
 if (img):     
     lista= random.sample(palab,k=cant)
     lista2=lista
     lista.extend(lista2)
 else:
     p1= list(palab[1])
     lista= random.sample(p1,k=cant)
     lista2=lista
     lista.extend(lista2)
 return lista    


def tablero (lista,event,img):
 l=''
 if (img):   
     if event.startswith("pieza-") :         
         if event == 'pieza-0-0':
             lista[0]=lista[0]
             l= lista[0]
         elif event == 'pieza-0-1':
             lista[3]=lista[3]
             l= lista[3]
         elif event == 'pieza-0-2':
             lista[4]=lista[4]
             l= lista[4]
         elif event == 'pieza-0-3':
             lista[1]=lista[1]
             l= lista[1]
         elif event == 'pieza-1-0':
             lista[2]=lista[2]
             l= lista[2]
         elif event == 'pieza-1-1':
             lista[7]=lista[7]
             l=lista[7]
         elif event == 'pieza-1-2':
             lista[6]=lista[6]             
             l=lista[6]
         elif event == 'pieza-1-3':
             lista[5]=lista[5]
             l=lista[5]
         elif event == 'pieza-2-0':
             lista[8]=lista[8]
             l=lista[8]
         elif event == 'pieza-2-1':
             lista[11]=lista[11]
             l=lista[11]
         elif event == 'pieza-2-2':
             lista[9]=lista[9]
             l=lista[9]
         elif event == 'pieza-2-3':
             lista[10]=lista[10]
             l=lista[10]
         elif event == 'pieza-3-0':
             lista[14]=lista[14]
             l=lista[14]
         elif event == 'pieza-3-1':
             lista[12]=lista[12]
             l=lista[12]
         elif event == 'pieza-3-2':
             lista[13]=lista[13]
             l=lista[13]
         elif event == 'pieza-3-3':
             lista[15]=lista[15]
             l=lista[15]                                            
 else:
     if event.startswith("pieza-") :         
         if event == 'pieza-0-0':
             lista[0]=lista[0][:7]
             l= lista[0].upper()
         elif event == 'pieza-0-1':
             lista[3]=lista[3][:7]
             l= lista[3].upper()
         elif event == 'pieza-0-2':
             lista[4]=lista[4][:7]
             l= lista[4].upper()
         elif event == 'pieza-0-3':
             lista[1]=lista[1][:7]
             l= lista[1].upper()
         elif event == 'pieza-1-0':
             lista[2]=lista[2][:7]
             l= lista[2].upper()
         elif event == 'pieza-1-1':
             lista[7]=lista[7][:7]
             l=lista[7].upper()
         elif event == 'pieza-1-2':
             lista[6]=lista[6][:7]             
             l=lista[6].upper()
         elif event == 'pieza-1-3':
             lista[5]=lista[5][:7]
             l=lista[5].upper()
         elif event == 'pieza-2-0':
             lista[8]=lista[8][:7]
             l=lista[8].upper()
         elif event == 'pieza-2-1':
             lista[11]=lista[11][:7]
             l=lista[11].upper()
         elif event == 'pieza-2-2':
             lista[9]=lista[9][:7]
             l=lista[9].upper()
         elif event == 'pieza-2-3':
             lista[10]=lista[10][:7]
             l=lista[10].upper()
         elif event == 'pieza-3-0':
             lista[14]=lista[14][:7]
             l=lista[14].upper()
         elif event == 'pieza-3-1':
             lista[12]=lista[12][:7]
             l=lista[12].upper()
         elif event == 'pieza-3-2':
             lista[13]=lista[13][:7]
             l=lista[13].upper()
         elif event == 'pieza-3-3':
             lista[15]=lista[15][:7]
             l=lista[15].upper()                                            
 return l            

def play(player, window, event, board_data,img):
    """
    Ejecuta una jugada sobre el tablero:
    - Actualiza el tablero visual
    - Agrega el valor en board_data
    - Chequea si hay un ganador
    """
    if (img):
     window[event].update(image_filename=player["value"],image_size=(90,90),button_color=colors.PRIMARY_LIGHT)
     _prefix, x, y = event.split("-")
     board_data[int(x)][int(y)] = player["value"]
    else:
     window[event].update(player["value"],image_filename=roja,image_size=(90,90),button_color=colors.PRIMARY_LIGHT)
     _prefix, x, y = event.split("-")
     board_data[int(x)][int(y)] = player["value"]
   
    return board_data


def pista_boton(c,window,cant):
 if cant == 4:
     if c == 1:
         window["pieza-0-3"].update(image_filename=pista,image_size=(90,90))
         window["pieza-1-3"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-3"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-1-3"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
     elif c == 2:     
         window["pieza-0-1"].update(image_filename=pista,image_size=(90,90))
         window["pieza-1-1"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-1"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-1-1"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
     elif c == 3:
         window["PISTA"].update(disabled=True)     
         window["pieza-0-0"].update(image_filename=pista,image_size=(90,90))
         window["pieza-0-2"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-0"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-0-2"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
 elif cant == 6:
     if c == 1:
         window["pieza-0-3"].update(image_filename=pista,image_size=(90,90))
         window["pieza-1-1"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-3"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-1-1"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
     elif c == 2:     
         window["pieza-0-0"].update(image_filename=pista,image_size=(90,90))
         window["pieza-1-2"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-0"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-1-2"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
     elif c == 3:
         window["PISTA"].update(disabled=True)     
         window["pieza-1-3"].update(image_filename=pista,image_size=(90,90))
         window["pieza-2-1"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-1-3"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-2-1"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
 elif cant == 8:
     if c == 1:
         window["pieza-0-0"].update(image_filename=pista,image_size=(90,90))
         window["pieza-2-0"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-0"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-2-0"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
     elif c == 2:     
         window["pieza-0-2"].update(image_filename=pista,image_size=(90,90))
         window["pieza-3-1"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-2"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-3-1"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()
     elif c == 3:
         window["PISTA"].update(disabled=True)     
         window["pieza-0-3"].update(image_filename=pista,image_size=(90,90))
         window["pieza-2-2"].update(image_filename=pista,image_size=(90,90))
         window.refresh()
         t.sleep(1)
         window["pieza-0-3"].update("",image_filename=cart,image_size=(110,100))
         window["pieza-2-2"].update("",image_filename=cart,image_size=(110,100))
         window.refresh()                        