from src.windows import inicio
from src.components import config, puntajes, estadisticas,jugar

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
        elif event == '-JUGAR-':
            jugar.start()

        window.un_hide()

    window.close()