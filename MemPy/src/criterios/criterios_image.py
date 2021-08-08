"""criterios para eleccion de fichas de juego"""
import datetime
from src.criterios.datasets import criterio_pokemon, criterio_simpsons
from src.criterios.datasets import criterio_anime

class Criterios_i:
    """Permite obtener los datos para las fichas según día y hora."""

    criterios = {
        0: {
                ('madrugada', ): criterio_pokemon.criterios['criterio4'],
                ('mañana', ): criterio_simpsons.criterios['criterio2'],
                ('tarde', ): criterio_pokemon.criterios['criterio3'],
                ('noche', ): criterio_anime.criterios['criterio1']  
            },
        1: {
                ('madrugada', ): criterio_pokemon.criterios['criterio1'],
                ('mañana', ): criterio_pokemon.criterios['criterio3'],
                ('tarde', ): criterio_simpsons.criterios['criterio1'],
                ('noche', ): criterio_anime.criterios['criterio1']
            },
        2: {
                ('madrugada', ): criterio_anime.criterios['criterio3'],
                ('mañana', ): criterio_pokemon.criterios['criterio4'],
                ('tarde', ): criterio_pokemon.criterios['criterio1'],
                ('noche', ): criterio_anime.criterios['criterio2']
            },
        3: {
                ('madrugada', ): criterio_simpsons.criterios['criterio2'],
                ('mañana', ): criterio_anime.criterios['criterio1'],
                ('tarde', ): criterio_pokemon.criterios['criterio4'],
                ('noche', ): criterio_simpsons.criterios['criterio1']  
            },
        4: {
                ('madrugada', ): criterio_pokemon.criterios['criterio5'],
                ('mañana', ): criterio_pokemon.criterios['criterio3'],
                ('tarde', ): criterio_simpsons.criterios['criterio2'],
                ('noche', ): criterio_anime.criterios['criterio3']  
            },
        5: {
                ('madrugada', ): criterio_pokemon.criterios['criterio5'],
                ('mañana', ): criterio_pokemon.criterios['criterio6'],
                ('tarde', ): criterio_simpsons.criterios['criterio1'],
                ('noche', ): criterio_anime.criterios['criterio2']
            },
        6: {
                ('madrugada', 'mañana'): criterio_pokemon.criterios['criterio6'],
                ('tarde', 'noche'): criterio_anime.criterios['criterio3'],
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
                lista_criterios = values['funcion']
                return (lista_criterios)

    @classmethod
    def seleccion_ahora(cls):
        """Retorna la selección de ahora."""
        return Criterios_i.seleccion_en(*cls.dia_semana_y_hora())

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
