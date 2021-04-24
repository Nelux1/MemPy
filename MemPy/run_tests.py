import unittest

# test cases
from src.servicio_usuarios.tests.test_user_repository import TestUsersRepository


if __name__=='__main__':
    suite = unittest.TestSuite((TestUsersRepository(), ))
    unittest.TextTestRunner().run(suite)