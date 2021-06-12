import PySimpleGUI as sg

from src.criterios.criterios import Criterios


dias = {
    'Lunes': 0, 
    'Martes': 1, 
    'Miércoles': 2, 
    'Jueves': 3, 
    'Viernes': 4, 
    'Sábado': 5, 
    'Domingo': 6
}

horas = {
    'Madrugada (0, 6)': 0,
    'Mañana (6, 12)': 6,
    'Tarde (12, 18)': 12,
    'Noche (18, 24)': 18
}


def mostrar_resultados(dia_semana, hora):
    """Muestra reusltados en una ventana de debug!"""
    criterio, resultados = Criterios.seleccion_en(dias[dia_semana], horas[hora])

    sg.easy_print(
        f'CRITERIO ---> {criterio}', *resultados,
        sep='\n',
        font=('times', 15)
    )

mostrar_resultados()