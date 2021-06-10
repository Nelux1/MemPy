import os
import json

from src.models.user import User

class UserRepository:
    """Realiza las operaciones de lectura/escritura de usuarios."""
    current_user = None
    json_path = os.path.join(os.getcwd(), 'users.json')

    @classmethod
    def get_usuarios(cls):
        """Retorna lista de usuarios.
        
            Si el json está vacío, retorna lista vacía.
        """
        with open(file=cls.json_path, mode='r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except:
                    pass
        return []
 
    @classmethod
    def obtener_usuario(cls, username):
        """Retorna un obj User si el usuario existe, None en caso contrario."""
        for usuario in cls.get_usuarios():
            if usuario['username'] == username:
                return User(**usuario)
        return None

    @classmethod
    def escribir_usuarios(cls, users):
        """"Escribe la lista de usuarios recibida por parámetros."""
        with open(file=cls.json_path, mode='w', encoding='utf-8') as f:
            json.dump(users, f)    

    @classmethod
    def obtener_puntaje(cls,puntaje):
       """Retorna un obj User el puntaje del usuario"""
       for points in cls.get_usuarios():
           if points['puntaje'] == puntaje:
               return User(**points)
       return None
    
    @classmethod
    def obtener_config(cls,configu):
       """Retorna un obj User el puntaje del usuario"""
       for conf in cls.get_usuarios():
           if conf['puntaje'] == configu:
               return User(**conf)
       return None

    @classmethod
    def escribir_puntaje(cls, points):
        """"Escribe la lista los puntajes de  los usuarios recibida por parámetros."""
        with open(file=cls.json_path, mode='w', encoding='utf-8') as f:
            json.dump(points, f)           
    
    @classmethod
    def agregar_usuario(cls, user):
        """Agrega el usuario al archivo json."""
        usuarios = cls.get_usuarios()
        usuarios.append(user.to_dict())
        cls.escribir_usuarios(usuarios)

    @classmethod
    def serializar_actual(cls):
        """Serializa los datos del usuario actual.
        
            Utilizar cuando se modifica algún dato del objeto current_user.
        """
        users = cls.get_usuarios()
        for i in range(len(users)):
            if users[i]['username'] == cls.current_user.username:
                users[i] = cls.current_user.to_dict()
                break
            if users[i]['puntaje'] == cls.current_user.puntaje:
                users[i] = cls.current_user.to_dict()
                break
            if users[i]['config'] == cls.current_user.config:
                users[i] = cls.current_user.to_dict()
                break
        cls.escribir_usuarios(users)