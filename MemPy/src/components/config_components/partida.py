from src.windows.config_windows import partida


def start():
    window = partida.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-CANCELAR-'):
            break

    window.close()