"""ventana de juego"""
from src.windows import popup , nivel
from src.windows import jugar
from src.components.tiempos import tiempos
import time as t

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
    print(configu[n]['-NIVEL-'])
    minutos= tiempos(configu,n)
    start_time= t.time()
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
            t_cada_paso= t_cada_paso + minutos               
            minutos= tiempos(configu)

        if timeformat == '-1:59':
         popup.build(configu[n]['-LOSS_MESSAGE-']).read()
         t.sleep(0.5)
         break
        
        realtime= t.time() - start_time
        minutos-= 1   
        window['-REAL_TIME-'].update(f'{round(realtime // 60):02d}:{round(realtime % 60):02d}')
        window['-TIMER-'].update(f'{timeformat}')
        niv= n + 1
        window['-NIV-'].update(f'{niv}')
        

    window.close()