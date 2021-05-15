from src.windows import popup

from src.windows.config_windows import estilos

from src.handlers import configuration_handlers


def start(nivel):
    event, values = estilos.build().read(close=True)

    if event not in ('-SALIR-', '-FIN-'):
        configuration_handlers.set_config_estilo(nivel, values['-TEMA-'])

        popup.build('Se guardó\ncorrectamente').read(close=True)