from src.servicio_usuarios.main.configuration import Configuration


class User:
    
    def __init__(self, username, gender=None, age=None, config=Configuration()):
        self.username = username
        self.gender = gender
        self.age = age
        self.config = config

    def __eq__(self, user):
        """Método creado para facilitar los tests.
        
            Dos objetos User son considerados iguales, si tienen
            el mismo username. Se supone que no debe haber
            repetidos en la BD.
        """
        if user:
            return self.username == user.username
        return False
    
    def __iter__(self):
        yield ('username', self.username)
        yield ('gender', self.gender)
        yield ('age', self.age)
        yield ('config', dict(self.config))