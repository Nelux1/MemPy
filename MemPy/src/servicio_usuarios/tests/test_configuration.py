import unittest

from src.servicio_usuarios.main.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    """TestCase para la clase Configuration."""
    
    
    def test_iter(self):
        self.assertEqual( {
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
        }, dict(Configuration()))
    
    def runTest(self):
        self.test_iter()