from pagina.baza_pagina import Baza
from selenium.webdriver.support.ui import WebDriverWait
from locators import DomowaStronaLocator
from selenium.webdriver.support import expected_conditions as EC


class StronaStartowa(Baza):

    def zaloguj_sie_button(self):
    # Kliknij "ZALOGUJ SIE"
        self.driver.find_element(*DomowaStronaLocator.guzik_zaloguj).click()

    def _verify_page(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(DomowaStronaLocator.guzik_zaloguj))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(DomowaStronaLocator.guzik_zaloguj))
        assert 'Roweria.pl - Sklep i Serwis Rowerowy Wrocław' in self.driver.title
        print('pierdu pierdu strona głowna')
