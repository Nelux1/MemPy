from src.windows import estadisticas


def start():
    window = estadisticas.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-BACK-'):
            break
        window.hide()

        if event == '-TOP-':
            top.start()
        elif event == '-PARTIDA-':
            part.start()
        else:
            genero.start()

        window.un_hide()
    window.close()

    window.close()