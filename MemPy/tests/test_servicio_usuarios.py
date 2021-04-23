"""Contiene tests para la clase UsersBD del modulo 
    servicio_usuarios.users.py
"""
import unittest

from src.servicio_usuarios import users

class TestUsersDB(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.db = users.UsersDB('./tests/dummy_users.json')
    
    def test_find_user(self):
        self.assertEqual('priscila', TestUsersDB.db.find_user('priscila')['username'])
        self.assertEqual(None, TestUsersDB.db.find_user('Priscila'))
        self.assertEqual(None, TestUsersDB.db.find_user(None))  
        self.assertEqual(None, TestUsersDB.db.find_user(''))
        
    def runTest(self):
        self.test_find_user()
