from src.windows import puntajes


def start():
    window = puntajes.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break

    window.close()