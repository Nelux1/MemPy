from src.windows import config_mensajes


def start():
    window = config_mensajes.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break

    window.close()