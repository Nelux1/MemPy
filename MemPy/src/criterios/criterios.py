
import datetime

from src.criterios.datasets import pokemon, marvel, dc, simpsons


class Criterios:
    """Permite obtener los datos para las fichas según día y hora."""

    criterios = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: {
                ('madrugada', ): pokemon.criterios['criterio1'],
                ('mañana', ): marvel.criterios['criterio1'],
                ('tarde', ): pokemon.criterios['criterio2'],
                ('noche', ): marvel.criterios['criterio2']  
            },
        5: {
                ('madrugada', ): dc.criterios['criterio1'],
                ('mañana', ): simpsons.criterios['criterio1'],
                ('tarde', ): pokemon.criterios['criterio3'],
                ('noche', ): dc.criterios['criterio2']
            },
        6: {
                ('madrugada', 'mañana'): simpsons.criterios['criterio2'],
                ('tarde', 'noche'): simpsons.criterios['criterio3'],
            }
    }

    horas = {
        (0, 6): 'madrugada',
        (6, 12): 'mañana',
        (12, 18): 'tarde',
        (18, 24): 'noche',
    }

    @classmethod
    def seleccion_ahora(cls):
        """Retorna una lista con los datos de hoy."""
        dia_semana, hora = cls.dia_semana_y_hora()

        rango_horario = cls.get_rango_horario(hora)
        seleccion_hoy = cls.criterios[dia_semana]

        for keys, values in seleccion_hoy.items():
            if rango_horario in keys:
                return values['funcion'](*values['parametros'])

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