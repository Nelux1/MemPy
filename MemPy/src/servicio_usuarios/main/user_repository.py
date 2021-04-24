import json

from .user import User
from .configuration import Configuration

    
class UserRepository:
    """Permite la conexión a una BD de usuarios.
    
        La base de datos es un archivo JSON.
    """

    def __init__(self, connection):
        """Crea una conexión a los archivos JSON.
        
        Parámetros
        ----------
            connection : str
             El filepath del archivo json sobre el que trabaja.
        """
        self.connection = connection
        
    def find_user(self, username):
        """Retorna un objeto User si existe el usuario o None.
        
        Parámetros
        ----------
            username : str
                El usuario que se está buscando
        """
        if username:
            with open(file=self.connection, mode='r', encoding='utf-8') as f:
                try:
                    users = json.load(f)
                    
                    for user in users:
                        if user['username'] == username:
                            return User(user['username'], user['gender'], user['age'], Configuration(user['config']))
                except:
                    pass
        return None
        
    
    def add_user(self, user):
        """Agrega el usuario a la BD.
        
        Parámetros
        ----------
            user : User
                El usuario que se va a agregar
        """
        pass
    
    def delete_user(self, username):
        """Elimina el usuario de la BD.
        
        Parámetros
        ----------
            username : str
                El usuario que se va a eliminar. 
        """
        pass
    
    def modify_user(self, username, **kwargs):
        """Modifica el usuario con los datos dados.
        
        Parámetros
        ----------
            username : str
                El usuario que se va a modificar .     
        """
        pass