import unittest

from tests.test_servicio_usuarios import TestUsersDB


if __name__=='__main__':
    suite = unittest.TestSuite((TestUsersDB(), ))
    unittest.TextTestRunner().run(suite)