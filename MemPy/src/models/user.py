import os
import json


class User:
    """Usuario de la aplicación."""

    def __init__(self, username, gender=None, age=None, puntaje=0, config=None):
        """Crea nuevo usuario."""

        # directorio donde obtiene configuraciones default.
        self.defaults = os.path.join(os.getcwd(), 'default_config.json')

        self.username = username
        self.gender = gender
        self.age = age
        self.puntaje = puntaje
        
        if not config:
            config = self.get_default_config()
        self.config = config
        

    def get_default_config(self):
        with open(file=self.defaults, mode='r', encoding='utf-8') as f:
            return json.load(f)        

    def to_dict(self):
        return {
            "username": self.username,
            "gender": self.gender,
            "age": self.age,
            "puntaje": self.puntaje,
            "config": self.config
        }