from selenium.webdriver.common.by import By

class DomowaStronaLocator():
    """ Selektory strony głównej"""
    guzik_zaloguj = (By.XPATH, '//a[@class="account_link link hidden-phone"]')
