"""ventana de juego"""
from src.criterios.criterios import Criterios
from src.windows import popup , nivel
from src.windows import jugar
from src.handlers.jugar_config import cuadros, tiempos, can_palabras_adivinar
from src.components.almacenamiento import guardando_data
import time as t
from datetime import datetime as dt

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
    dia_hora= dt.now().date()
    criterio=Criterios.seleccion_ahora()
    for crit in criterio:
     print(crit)
    cronometro=0
    t_cada_paso= 0
    cant_de_palabras= can_palabras_adivinar(cuadros(configu,n))
    evento='Inicio de partida'
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
            window[event].update('DAMOS VUELTA')
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
        window['-DIA-HORA-'].update(f'{dia_hora}')   
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
    print(guardando_data(username,age,gender, realtime,num_de_partida,niv,cant_de_palabras,evento,estado,palabra))
    window.close()