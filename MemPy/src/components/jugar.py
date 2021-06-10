from warnings import simplefilter
from src.windows import jugar
from src.components.tiempos import tiempos
import time as t

def start(username,configu):
    window = jugar.build(username,configu)
    
    minutos= tiempos(configu)
    start_time= t.time()

    while True:
        event, values = window.read(timeout=1000)
        
        mins, secs = divmod(minutos, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        if event == '-SALIR-':
            break
        elif event.startswith("pieza-") :
            pieza,cord= event.split('-')
            print(f'{pieza}{cord}')
            minutos= tiempos(configu)
            
        realtime= t.time() - start_time
        minutos-= 1
        window['-REAL_TIME-'].update(f'{round(realtime // 60):02d}:{round(realtime % 60):02d}')
        window['-TIMER-'].update(f'{timeformat}')
    
    window.close()