from src.windows import popup
from src.windows.config_windows import partida

from src.handlers import configuration_handlers


def start(nivel):
    event, values = partida.build().read(close=True)

    if event not in ('-SALIR-', '-FIN-'):
        configuration_handlers.set_config_partida(
            nivel, 
            values['-CASILLAS-'], 
            values['-COINCIDENCIAS-'], 
            values['-ELEMENTOS-'], 
            values['-TIEMPO_MIN-'], 
            values['-PISTAS-']
        )

        popup.build('Se guardó\ncorrectamente').read(close=True)