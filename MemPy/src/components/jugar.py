"""ventana de juego"""
from calendar import c

from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from src.criterios.criterios import Criterios
from src.criterios.criterios_image import Criterios_i 
from src.windows import popup , nivel
from src.windows import jugar
from src.handlers.palabras_fichas import play, tablero , palabras , pista_boton 
from src.handlers.jugar_config import cuadros, tiempos, can_palabras_adivinar
from src.components.almacenamiento import guardando_data, puntos
import time as t
import os
from src.windows import colors

pista=os.path.join(
    'resources',
    'icons',
    'outline_home_black_48dp.png'

)
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

def start(username,configu,age,gender,puntaje):
    
    num_de_partida=1

    window2= nivel.popup_nivel()
    while True:
      event,_values= window2.read()
      if event == 'Nivel 1':
          n= 0          
          break
      elif event == 'Nivel 2':
          n=1
          break
      elif event == 'Nivel 3':
          n=2
          break
    window2.close()    
       
    dia_hora=Criterios.dia_semana_y_hora()
    minutos= tiempos(configu,n)
    start_time= t.time()
    img=True
    criterio=[]
    if configu[n]["-ELEMENTOS-"] == "Imagenes":  
     criterio=Criterios_i.seleccion_ahora()
    elif configu[n]["-ELEMENTOS-"] == "Palabras":
     criterio=Criterios.seleccion_ahora()
     img=False 
    dia = dia_hora[0]
    hora = dia_hora[1]
    cronometro=0
    t_cada_paso= 0
    cant_de_palabras= can_palabras_adivinar(cuadros(configu,n))
    evento='Inicio_partida'
    estado=''
    palabra=''
    niv= n + 1
    realtime=t.time()  
    guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia,hora)
    palabra2=''
    p,p2='',''
    toque=0
    c=0
    board_data= [[" "]* 4 for _i in range (cuadros(configu,n))]
    window = jugar.build(username,configu,n,board_data)
    toque=0
    encontrada=0
    lista=palabras(cant_de_palabras,criterio,img)
    print(lista)

    while True:
        event, _values = window.read(timeout=1000)       
        player={"value":tablero(lista,event,img)}
        mins, secs = divmod(minutos, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        if event == '-SALIR-':
            evento='cancelada'
            puntaje=0
            break
        elif event.startswith("pieza-") :       
            toque+=1
            puntaje+=1
            board_data=play(player,window,event,board_data,img)
            window.refresh()
            t.sleep(1)
            window.refresh()
            if toque == 1:
             palabra=player["value"]
             p=event
            if toque == 2:  
             palabra2= player["value"]
             p2=event    
             toque=0
             if palabra != palabra2:
                 estado='error'
                 evento='intento'
                 guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia,hora)    
                 t.sleep(0.5)
                 window[p].update("",image_filename=cart,image_size=(110,100),button_color=(colors.BACKGROUND,colors.WHITE))
                 window[p2].update("",image_filename=cart,image_size=(110,100),button_color=(colors.BACKGROUND,colors.WHITE))
                 window.refresh()
             elif palabra == palabra2:
                 estado='ok'
                 evento='intento'
                 guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia,hora)
                 encontrada+=1
                 t.sleep(0.5)
                 puntaje+=10
                 window[p].update("",image_filename=acierto,image_size=(110,100),disabled=True,button_color=(colors.BACKGROUND,colors.WHITE))
                 window[p2].update("",image_filename=acierto,image_size=(110,100),disabled=True,button_color=(colors.BACKGROUND,colors.WHITE))    
            t_cada_paso= cronometro + t_cada_paso
            cronometro=0                
            minutos= tiempos(configu,n)
            window['-POCO-TIEMPO-'].update(visible=False) 
        elif event == "-ABANDONAR-":
            popup.build('USTED A ABANDONADO LA PARTIDA!\n perdera los puntos ganados').read(close=True)
            evento='abandonada'
            palabra=''
            guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia,hora)
            puntaje=0
            break
        realtime= t.time() - start_time
        cronometro+=1
        minutos-= 1      
        window['-REAL_TIME-'].update(f'{round(realtime // 60):02d}:{round(realtime % 60):02d}')
        window['-TIMER-'].update(f'{timeformat}')
        window['-TIEMPO-PASO-'].update(f'{round(t_cada_paso // 60):02d}:{round(t_cada_paso % 60):02d}')
        window['-NIV-'].update(f'{niv}')
        window['-ENCONTRADOS-'].update(f'{encontrada} de {cant_de_palabras}')
        
        if timeformat == '00:00':
         popup.build(configu[n]['-LOSS_MESSAGE-']).read(close=True)
         num_de_partida+=1
         evento='fin'
         estado='timeout'
         palabra=''
         guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia,hora)
         puntaje=0
         break   
        if timeformat == '00:10':
         window['-POCO-TIEMPO-'].update(visible=True)
        if encontrada == cant_de_palabras:
           popup.build(configu[n]['-WIN_MESSAGE-']).read(close=True)
           if t_cada_paso < 30.00:
             puntaje+=1000
           elif t_cada_paso < 60.00:
             puntaje+=500      
           evento='fin'
           estado='finalizada'
           palabra=''
           puntaje+=50
           guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia,hora)
           break
        if event == 'PISTA':
         puntaje-=20   
         c+=1
         pista_boton(c,window,cant_de_palabras)
    print(puntos(username,puntaje))
    window.close()