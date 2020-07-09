import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://roweria.pl')
        self.driver.maximize_window()
        #tutaj do dopytania co robi globalnie ten emplicit
        self.driver.implicitly_wait(30)
        self.driver.delete_all_cookies()


    @classmethod
    def tearDown(self):
        self.driver.quit()
