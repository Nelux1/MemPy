from src.windows.config_windows import mensajes


def start():
    window = mensajes.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-CANCELAR-'):
            break

    window.close()