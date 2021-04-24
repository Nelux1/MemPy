import unittest

from src.servicio_usuarios.main.user import User


class TestUser(unittest.TestCase):
    """TestCase para la clase User."""
    
    
    def test_iter(self):
        self.assertEqual({
        "username": "priscila",
        "gender": "mujer",
        "age": 21,
        "config": {
            "win_message": "¡Ganaste!",
            "loss_message": "¡Perdiste!",
            "grid_size_per_level": [
                8,
                16,
                20
            ],
            "coincidences": 2,
            "elements_type": "imagenes",
            "hints": True,
            "time": 180,
            "theme": "dark blue 1"
        }
    }, dict(User('priscila', 'mujer', 21)))
    
    def runTest(self):
        self.test_iter()