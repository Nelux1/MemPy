from src.windows import estadisticas


def start():
    window = estadisticas.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break

    window.close()