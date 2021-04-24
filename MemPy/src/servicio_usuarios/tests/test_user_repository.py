import unittest

from src.servicio_usuarios.main import user_repository
from src.servicio_usuarios.main.user import User


FILEPATH_TESTING_FILE = 'MemPy/src/servicio_usuarios/tests/dummy_users.json'

class TestUsersRepository(unittest.TestCase):
    """Test Case para la clase UserRepository"""

    @classmethod
    def setUpClass(cls):
        cls.db = user_repository.UserRepository(FILEPATH_TESTING_FILE)
    
    def test_find_user(self):
        self.assertEqual(User('priscila'), TestUsersRepository.db.find_user('priscila'))
        self.assertEqual(None, TestUsersRepository.db.find_user('Priscila'))
        self.assertEqual(None, TestUsersRepository.db.find_user(None))  
        self.assertEqual(None, TestUsersRepository.db.find_user(''))
        
    def runTest(self):
        self.test_find_user()
