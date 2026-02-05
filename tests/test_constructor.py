from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructor:

    def test_switch_to_sauces(self, login):

        driver = login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_TAB))

        driver.find_element(*Locators.SAUCES_SECTION).click()

        active_tab = driver.find_element(*Locators.ACTIVE_TAB)

        assert "Соусы" in active_tab.text
        driver.quit()

    def test_switch_to_filling(self, login):

        driver = login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_TAB))

        driver.find_element(*Locators.FILLING_SECTION).click()

        active_tab = driver.find_element(*Locators.ACTIVE_TAB)

        assert "Начинки" in active_tab.text
        driver.quit()

    def test_switch_to_buns(self, login):

        driver = login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_TAB))

        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()

        active_tab = driver.find_element(*Locators.ACTIVE_TAB)

        assert "Булки" in active_tab.text
        driver.quit()






