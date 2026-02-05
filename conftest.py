import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from curl import *
from locators import Locators
from data import Credentials

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})

    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):

    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN).click()

    return driver