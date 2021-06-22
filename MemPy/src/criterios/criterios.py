"""criterios para eleccion de fichas de juego"""
import datetime
import random
from src.criterios.datasets import pokemon, marvel, dc, simpsons
from src.criterios.datasets import steam, tv_shows, spotify, disney


class Criterios:
    """Permite obtener los datos para las fichas según día y hora."""

    criterios = {
        0: {
                ('madrugada', ): steam.criterios['criterio1'],
                ('mañana', ): spotify.criterios['criterio1'],
                ('tarde', ): disney.criterios['criterio1'],
                ('noche', ): tv_shows.criterios['criterio1']  
            },
        1: {
                ('madrugada', ): spotify.criterios['criterio2'],
                ('mañana', ): steam.criterios['criterio2'],
                ('tarde', ): tv_shows.criterios['criterio2'],
                ('noche', ): disney.criterios['criterio2']
            },
        2: {
                ('madrugada', ): tv_shows.criterios['criterio3'],
                ('mañana', ): steam.criterios['criterio3'],
                ('tarde', ): spotify.criterios['criterio3'],
                ('noche', ): disney.criterios['criterio3']
            },
        3: {
                ('madrugada', ): spotify.criterios['criterio4'],
                ('mañana', ): tv_shows.criterios['criterio4'],
                ('tarde', ): disney.criterios['criterio4'],
                ('noche', ): steam.criterios['criterio4']  
            },
        4: {
                ('madrugada', ): pokemon.criterios['criterio1'],
                ('mañana', ): marvel.criterios['criterio1'],
                ('tarde', ): pokemon.criterios['criterio2'],
                ('noche', ): marvel.criterios['criterio2']  
            },
        5: {
                ('madrugada', ): dc.criterios['criterio1'],
                ('mañana', ): spotify.criterios['criterio5'],
                ('tarde', ): pokemon.criterios['criterio3'],
                ('noche', ): dc.criterios['criterio2']
            },
        6: {
                ('madrugada', 'mañana'): spotify.criterios['criterio6'],
                ('tarde', 'noche'): steam.criterios['criterio3'],
            }
    }

    horas = {
        (0, 6): 'madrugada',
        (6, 12): 'mañana',
        (12, 18): 'tarde',
        (18, 24): 'noche',
    }

    @classmethod
    def seleccion_en(cls, dia_semana, hora):
        """Retorna la seleccion reducida de palabras para el dia y la hora dadas.
        
            Parametros
            ---------
                dia_semana : int
                    entre 0 y 6, siendo lunes el 0
                hora : int
                    entre 0 y 24
            
            Return 
            ------
                tuple -> (<nombre del criterio> : str, <lista de resultados> : list)
        """
        rango_horario = cls.get_rango_horario(hora)
        seleccion_hoy = cls.criterios[dia_semana]
        for keys, values in seleccion_hoy.items():
            if rango_horario in keys:
                lista_criterios = values['funcion'](*values['parametros'])
                lista_reducida_criterios = random.sample(lista_criterios, k=8)
                return (values['criterio'], lista_reducida_criterios)

    @classmethod
    def seleccion_ahora(cls):
        """Retorna la selección de ahora."""
        return Criterios.seleccion_en(*cls.dia_semana_y_hora())

    @classmethod
    def dia_semana_y_hora(cls):
        """Retorna una tupla (int(weekday), int(hour))"""
        hoy = datetime.datetime.today()
        return (hoy.weekday(), hoy.time().hour)

    @classmethod
    def get_rango_horario(cls, hora):
        """Retorna el nombre del rango correspondiente a la hora recibida.
        
            Ejemplo -> hora = 3, return: 'madrugada'
        """
        for keys, values in cls.horas.items():
            if hora >= keys[0] and hora < keys[1]:
                return values

