class Configuration:
    """Clase para encapsular las configuraciones de un usuario."""

    def __init__(self, config=None):
        """
            Parámetros:
            ---------
                config : dict
                    Un diccionario que tiene keys de las 
                    que se puede ver en el archivo
                    default_config.json en el objeto "config".
        """
        self.set_default_config()
        if config:
            self.set_config(**config)

    def set_default_config(self):
        self.win_message = '¡Ganaste!'
        self.loss_message = '¡Perdiste!'
        self.grid_size_per_level = [8, 16, 20]
        self.coincidences = 2
        self.elements_type = "imagenes"
        self.hints = True
        self.time = 180
        self.theme = "dark blue 1"

    def set_config(self, **kwargs):
        """Setea las configuraciones enviadas en kwargs"""
        for key, value in kwargs.items():
            self.__dict__[key] = value
            
    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key, value)