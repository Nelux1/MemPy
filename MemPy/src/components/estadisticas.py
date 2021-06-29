from src.windows import estadisticas
from src.components import graficos


def start():
    window = estadisticas.build()

    while True:
        event, values = window.read()
        if event in ('-SALIR-', '-BACK-'):
            break
        window.hide()

        if event == 'Top 10 palabras':
            break
        elif event == '-PARTIDA-':
            graficos.porcentaje_por_estado()
        elif event == '-GENERO-':
            graficos.porcentaje_por_estado()

        window.un_hide()
    window.close()

    window.close()