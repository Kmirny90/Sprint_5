from curl import *
from locators import Locators
from data import Credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def test_login_from_main_page(self, driver):

        driver.get(main_site)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()


    def test_login_personal_account(self, driver):

        driver.get(main_site)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()


    def test_login_register_page(self, driver):

        driver.get(register_page)
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTER).click()

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()


    def test_login_recover_password(self, driver):

        driver.get(forgot_password_page)
        driver.find_element(*Locators.LOGIN_FORGOT_PASSWORD).click()

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()
