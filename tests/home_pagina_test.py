from tests.baza_test import BaseTest
import unittest
from pagina.strona_glowna import StronaStartowa

class TestPaginyHome(BaseTest):
    #driver = self.driver
    def zly_majl(self):
        StronaStartowa(self.driver).zaloguj_sie_button()


if __name__=="__main__":
    unittest.main(verbosity=2)