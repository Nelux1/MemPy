import os
import json


class User:
    """Usuario de la aplicación."""

    def __init__(self, username, gender=None, age=None):
        """Crea nuevo usuario con configuraciones default."""
        self.defaults = os.path.join(os.getcwd(), 'default_config.json')

        self.username = username
        self.gender = gender
        self.age = age
        
        self.set_default_config()

    def set_default_config(self):
        with open(file=self.defaults, mode='r', encoding='utf-8') as f:
            defaults = json.load(f)
            self.config = defaults

    def to_json(self):
        return {
            "username": self.username,
            "gender": self.gender,
            "age": self.age,
            "config": self.config
        }