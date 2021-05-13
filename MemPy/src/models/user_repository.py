import os
import json

    
class UserRepository:
    """Realiza las operaciones de lectura/escritura de usuarios."""

    def __init__(self):
        """Se 'conecta' al archivo .json de los usuarios."""
        self.json_path = os.path.join(os.getcwd(), 'users.json')

    def get_usuarios(self):
        """Retorna lista de usuarios.
        
            Si el json está vacío, retorna lista vacía.
        """
        with open(file=self.json_path, mode='r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except:
                    pass
        return []

    def existe_usuario(self, username):
        """Retorna True si el usuario existe, false en caso contrario."""
        usuarios = self.get_usuarios()
        for usuario in usuarios:
            if usuario['username'] == username:
                return True
        return False
        
    def agregar_usuario(self, user):
        """Agrega el usuario al archivo json.
        
        Parámetros
        ----------
            user : User
                El usuario que se va a agregar
        """
        usuarios = self.get_usuarios()
        usuarios.append(user.to_json())
        with open(file=self.json_path, mode='w', encoding='utf-8') as f:
            json.dump(usuarios, f)