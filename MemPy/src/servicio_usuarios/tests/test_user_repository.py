import unittest

from src.servicio_usuarios.main import user_repository
from src.servicio_usuarios.main.user import User


FILEPATH_TESTING_FILE = 'src/servicio_usuarios/tests/dummy_users.json'

class TestUsersRepository(unittest.TestCase):
    """Test Case para la clase UserRepository"""

    @classmethod
    def setUpClass(cls):
        cls.db = user_repository.UserRepository(FILEPATH_TESTING_FILE)
    
    def test_find_user(self):
        # Existe en dummy_users.json
        self.assertEqual(User('priscila'), TestUsersRepository.db.find_user('priscila'))
        # No existe en dummy_users.json
        self.assertEqual(None, TestUsersRepository.db.find_user('Federico'))
        self.assertEqual(None, TestUsersRepository.db.find_user(None))  
        self.assertEqual(None, TestUsersRepository.db.find_user(''))
        
    def test_add_user(self):
        self.assertTrue(True, TestUsersRepository.db.add_user(User('Priscila', 'mujer', 21)))
        self.assertTrue(True, TestUsersRepository.db.add_user(User('Ezequiel', 'mujer', 21)))
        
    def runTest(self):
        self.test_find_user()
        self.test_add_user()
