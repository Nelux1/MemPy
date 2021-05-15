from src.windows import popup

from src.windows.config_windows import mensajes

from src.handlers import configuration_handlers


def start(nivel):
    event, values = mensajes.build().read(close=True)

    if event not in ('-SALIR-', '-FIN-'):
        configuration_handlers.set_config_mensajes(
            nivel, 
            values['-WIN_MESSAGE-'], 
            values['-LOSS_MESSAGE-'], 
            values['-TIMELEFT_MESSAGE-']
        )

        popup.build('Se guardó\ncorrectamente').read(close=True)