from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import login_page
from locators import Locators
from data import Credentials


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):

        driver.get(login_page)

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_REGISTERED_USER).click()

        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert "profile" in driver.current_url
        driver.quit()

    def test_go_from_account_to_constructor(self, driver):
        driver.get(login_page)

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_REGISTERED_USER).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()
        driver.quit()

    def test_go_from_account_to_constructor_logo(self, driver):
        driver.get(login_page)

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_REGISTERED_USER).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()
        driver.quit()

    def test_logout_from_account(self, driver):
        driver.get(login_page)

        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON_REGISTERED_USER).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url