import unittest

# test cases
from src.servicio_usuarios.tests.test_user_repository import TestUsersRepository
from src.servicio_usuarios.tests.test_configuration import TestConfiguration
from src.servicio_usuarios.tests.test_user import TestUser


if __name__=='__main__':
    suite = unittest.TestSuite((TestUsersRepository(), TestConfiguration(), TestUser()))
    unittest.TextTestRunner().run(suite)