from pagina.baza_page import Baza
from selenium.webdriver.support.ui import WebDriverWait
from locators import Domowa_strona_locator
from selenium.webdriver.support import expected_conditions as EC


class Strona_startowa(Baza):

    def zaloguj_sie_button(self):
    # Kliknij "ZALOGUJ SIE"
        guzik = self.driver.find_element(*Domowa_strona_locator.guzik_zaloguj).click()

    def _verify_page(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(Domowa_strona_locator.guzik_zaloguj))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Domowa_strona_locator.guzik_zaloguj))
        assert 'Roweria.pl - Sklep i Serwis Rowerowy Wrocław' in self.driver.title
        Print('pierdu pierdu strona głowna')
