from src.windows import inicio
from src.components import config

def start():
    window = inicio.build()
    
    while True:
        event, values = window.read()
        
        if event == '-SALIR-':
            break
        
        window.hide()

        if event == '-CONFIG-':
            config.start()

        window.un_hide()

    window.close()