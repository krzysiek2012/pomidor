import unittest
from tests.home_pagina_test import TestPaginyHome

# Pobierz test, które chcesz uruchomić
tescigpaginy_test_1 = unittest.TestLoader().loadTestsFromTestCase(TestPaginyHome)


# Stwórz Test Suita
test_suite = unittest.TestSuite([tescigpaginy_test_1])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)