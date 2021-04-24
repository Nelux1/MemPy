"""Contiene tests para la clase UsersBD del modulo 
    servicio_usuarios.users.py
"""
import unittest

# test cases
from src.servicio_usuarios import user_repository

# other
from src.servicio_usuarios.user import User


class TestUsersDB(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.db = user_repository.UserRepository('MemPy/tests/dummy_users.json')
    
    def test_find_user(self):
        self.assertEqual(User('priscila'), TestUsersDB.db.find_user('priscila'))
        self.assertEqual(None, TestUsersDB.db.find_user('Priscila'))
        self.assertEqual(None, TestUsersDB.db.find_user(None))  
        self.assertEqual(None, TestUsersDB.db.find_user(''))
        
    def runTest(self):
        self.test_find_user()
