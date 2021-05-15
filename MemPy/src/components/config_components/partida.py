from src.windows.config_windows import partida
from src.components import config_json

def start(nivel):
    window = partida.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-CANCELAR-'):
            break
        if event == '-GUARDAR-':
         casillas= values['-CASILLAS-']
         coincidencias=values['-COINCIDENCIAS-']
         elementos= values['-ELEMENTOS-']
         tiempo= values['-TIEMPO-']
         pistas=values['-PISTAS-']         
         config_json.set_config_partida(nivel,casillas,coincidencias,elementos,tiempo,pistas)
        break  
    window.close()