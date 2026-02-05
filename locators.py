from selenium.webdriver.common.by import By

class Locators:
    #test_registration
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input") #Поле Имя
    EMAIL_REGISTER = (By.XPATH, "//label[text()='Email']/following-sibling::input") #Поле Email
    PASSWORD_REGISTER =(By.XPATH, "//label[text()='Пароль']/following-sibling::input") #Поле Password
    REGISTER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") #Кнопка Зарегистрироваться
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']") #Сообщение об ошибке
    #test_login
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") #Поле Email
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") #Поле Password
    LOGIN = (By.XPATH, "//button[text()='Войти']") #Кнопка Войти
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") #Кнопка Оформить заказ
    PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[href='/account']") #Кнопка Личный Кабинет
    LOGIN_BUTTON_REGISTER = (By.CSS_SELECTOR, ".Auth_link__1fOlj") #Кнопка Войти на странице регистрации
    LOGIN_FORGOT_PASSWORD = (By.CSS_SELECTOR, ".Auth_link__1fOlj") #Кнопка Войти на странице восстановления пароля
    #test_personal_account
    PERSONAL_ACCOUNT_BUTTON_REGISTERED_USER = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка Личный Кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") #Кнопка Конструктор
    LOGO_BUTTON = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2") #Кнопка Логотип
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #Кнопка Выход
    #test_constructor
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']") #Переход к соусам
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']") #Переход к начинкам
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']") #Переход к булкам
    ACTIVE_TAB = (By.CSS_SELECTOR, "[class*='tab_tab_type_current__2BEPc']")