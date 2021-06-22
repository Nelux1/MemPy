"""ventana de juego"""
from src.criterios.criterios import Criterios
from src.windows import popup , nivel
from src.windows import jugar
from src.handlers.jugar_config import cuadros, tiempos, can_palabras_adivinar
from src.components.almacenamiento import guardando_data
from src.handlers.eleccion_palabras import palabras
import time as t
from src.windows import colors
from datetime import datetime as dt
import os

ficha= os.path.join(
    'resources', 
    'icons', 
    'outline_close_black_48dp.png'
)

def start(username,configu,age,gender):
    
   
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
    
   
    window = jugar.build(username,configu,n)
    
    minutos= tiempos(configu,n)
    start_time= t.time()
    dia_hora= Criterios.dia_semana_y_hora()
    criterio=Criterios.seleccion_ahora()
    for crit in criterio:
     print(crit)
    cronometro=0
    t_cada_paso= 0
    cant_de_palabras= can_palabras_adivinar(cuadros(configu,n))
    print('\nLISTA DE PALABRAS REPETIDAS\n')
    palabras(cant_de_palabras,criterio)
    evento='Inicio_partida'
    estado='ok'

    while True:
        event, _values = window.read(timeout=1000)
        
        mins, secs = divmod(minutos, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)

        if event == '-SALIR-':
            break
        elif event.startswith("pieza-") :
            pieza,cord= event.split('-')
            print(f'{pieza}: {cord}')
            window[event].update('DAMOS',image_filename=None,button_color=colors.BLACK)
            """FUNCION QUE COMPRUEBA PIEZA CON PIEZA"""
            t_cada_paso= cronometro + t_cada_paso
            cronometro=0                
            minutos= tiempos(configu,n)
            window['-POCO-TIEMPO-'].update(visible=False) 
            estado='ok'
       

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
         break   
        if timeformat == '00:10':
         window['-POCO-TIEMPO-'].update(visible=True)
        
    palabra='todavia no hay'
    print(guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra,dia_hora))
    window.close()