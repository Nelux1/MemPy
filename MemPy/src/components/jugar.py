"""ventana de juego"""
from src.criterios.criterios import Criterios
from src.windows import popup , nivel, puntajes
from src.windows import jugar
from src.handlers.eleccion_palabras import play, tablero , palabras
from src.handlers.jugar_config import cuadros, tiempos, can_palabras_adivinar
from src.components.almacenamiento import guardando_data, puntos
import time as t
from itertools import cycle
import os

cart= os.path.join(
    'resources', 
    'icons', 
    'inte.png'
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
       
    
    minutos= tiempos(configu,n)
    start_time= t.time()
    dia_hora= Criterios.dia_semana_y_hora()
    criterio=Criterios.seleccion_ahora()
    cronometro=0
    t_cada_paso= 0
    cant_de_palabras= can_palabras_adivinar(cuadros(configu,n))
    evento='Inicio_partida'
    estado='ok'
    
    board_data= [[" "]* 4 for _i in range (cuadros(configu,n))]

    window = jugar.build(username,configu,n,board_data)
    toque=0
    lista=palabras(cant_de_palabras,criterio)
    

    while True:
        event, _values = window.read(timeout=1000)
        
        player_1={"value":tablero(lista,event)}
        player_2={"value": ''}

        turn=cycle([player_1,player_2])
        
        mins, secs = divmod(minutos, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        if event == '-SALIR-':
            evento='cancelada'
            break
        elif event.startswith("pieza-") :
            player=next(turn)
            #_prefix,x ,y= event.split("-")
            #print(f'pieza: {x},{y}')
            board_data=play(player,window,event,board_data,toque)
            window.refresh()
            toque+=1
            puntaje+=1
            if toque == 2:
             t.sleep(1)
             window[event].update('',image_filename=cart,image_size=(70,70))
             window.refresh()
            t_cada_paso= cronometro + t_cada_paso
            cronometro=0                
            minutos= tiempos(configu,n)
            window['-POCO-TIEMPO-'].update(visible=False) 
            estado='ok'
        elif event == "-ABANDONAR-":
            popup.build('USTED A ABANDONADO LA PARTIDA!\n perdera los puntos ganados').read(close=True)
            evento='abandonada'
            puntaje=0
            break
        realtime= t.time() - start_time
        cronometro+=1
        minutos-= 1
        niv= n + 1        
        window['-REAL_TIME-'].update(f'{round(realtime // 60):02d}:{round(realtime % 60):02d}')
        window['-TIMER-'].update(f'{timeformat}')
        window['-TIEMPO-PASO-'].update(f'{round(t_cada_paso // 60):02d}:{round(t_cada_paso % 60):02d}')
        window['-NIV-'].update(f'{niv}')
        
        if timeformat == '00:00':
         popup.build(configu[n]['-LOSS_MESSAGE-']).read(close=True)
         num_de_partida+=1
         evento='Tiempo agotado'
         puntaje=0
         break   
        if timeformat == '00:10':
         window['-POCO-TIEMPO-'].update(visible=True)
        
    palabra='todavia no hay'
    print(guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia_hora))
    print(puntos(username,puntaje))
    window.close()