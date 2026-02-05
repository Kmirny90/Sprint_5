from helper import generate_registration_data
from locators import Locators
from curl import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationNewCredentials:

    def test_success_registration(self, driver):

        driver.get(register_page)
        name, email, password, shot_password = generate_registration_data()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTER).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_page))

        assert "login" in driver.current_url



    def test_registration_with_short_password(self, driver):

        driver.get(register_page)
        name, email, password, short_password = generate_registration_data()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_REGISTER).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REGISTER).send_keys(short_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()


        error_elements = driver.find_element(*Locators.PASSWORD_ERROR).text
        assert error_elements == 'Некорректный пароль'




