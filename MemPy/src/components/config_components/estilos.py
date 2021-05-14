from src.windows.config_windows import estilos


def start():
    window = estilos.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-CANCELAR-'):
            break

    window.close()