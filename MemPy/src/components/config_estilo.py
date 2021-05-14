from src.windows import config_estilo


def start():
    window = config_estilo.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break

    window.close()