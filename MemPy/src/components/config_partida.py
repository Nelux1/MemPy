from src.windows import config_partida


def start():
    window = config_partida.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break

    window.close()