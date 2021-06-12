"""ventana de juego"""
from src.criterios.criterios import Criterios
from src.windows import popup , nivel
from src.windows import jugar
from src.components.jugar_config import mensajes, tiempos
import time as t
from datetime import datetime as dt

def start(username,configu):
    
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
    dia_hora= dt.now()
    criterio=Criterios.seleccion_ahora()
    print(criterio)
    cronometro=0
    t_cada_paso= 0
   

    while True:
        event, _values = window.read(timeout=1000)
        
        mins, secs = divmod(minutos, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)

        if event == '-SALIR-':
            break
        elif event.startswith("pieza-") :
            pieza,cord= event.split('-')
            print(f'{pieza}: {cord}')
            t_cada_paso= cronometro + t_cada_paso
            cronometro=0                
            minutos= tiempos(configu,n)
            window['-POCO-TIEMPO-'].update(visible=False) 
            
        if timeformat == '-1:59':
         popup.build(configu[n]['-LOSS_MESSAGE-']).read(close=True)
         break   
        if timeformat == '00:10':
         window['-POCO-TIEMPO-'].update(visible=True)

        realtime= t.time() - start_time
        cronometro+=1
        minutos-= 1
        niv= n + 1       
        window['-DIA-HORA-'].update(f'{dia_hora}')   
        window['-REAL_TIME-'].update(f'{round(realtime // 60):02d}:{round(realtime % 60):02d}')
        window['-TIMER-'].update(f'{timeformat}')
        window['-TIEMPO-PASO-'].update(f'{round(t_cada_paso // 60):02d}:{round(t_cada_paso % 60):02d}')
        window['-NIV-'].update(f'{niv}')
        

    window.close()