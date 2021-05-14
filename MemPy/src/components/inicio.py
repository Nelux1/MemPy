from src.windows import inicio
from src.components import config, puntajes, estadisticas

def start():
    window = inicio.build()
    
    while True:
        event, values = window.read()
        
        if event == '-SALIR-':
            break
        
        window.hide()

        if event == '-CONFIG-':
            config.start()
        elif event == '-ESTADISTICAS-':
            estadisticas.start()
        elif event == '-PUNTAJES-':
            puntajes.start()
        else: # -JUGAR-
            pass

        window.un_hide()

    window.close()