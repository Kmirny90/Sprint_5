# Sprint_5 - Автотесты для Stellar Burgers

## Описание проекта
Автотесты на Selenium для тестирования функционала сайта Stellar Burgers.

## Технологии
- Python 3.14
- Selenium 4.x
- Pytest
- Google Chrome

## Структура проекта
Sprint_5/
├── tests/
│ ├── test_registration.py
│ ├── test_login.py
│ ├── test_personal_account.py
│ └── test_constructor.py
├── locators.py
├── conftest.py
├── helper.py
├── data.py
├── curl.py
├── requirements.txt
├── .gitignore
└── README.md

### Тесты
- `tests/test_registration.py` - тесты регистрации (успешная и с ошибкой пароля)
- `tests/test_login.py` - тесты входа в аккаунт разными способами
- `tests/test_personal_account.py` - тесты личного кабинета
- `tests/test_constructor.py` - тесты конструктора бургеров

### Вспомогательные файлы
- `conftest.py` - фикстуры Pytest (инициализация браузера)
- `locators.py` - локаторы для поиска элементов на странице
- `helper.py` - генераторы тестовых данных
- `data.py` - тестовые данные (учётные данные существующего пользователя)
- `curl.py` - константы URL страниц
- `requirements.txt` - зависимости проекта

## Установка и запуск

### 1. Установка зависимостей:

```bash
pip install -r requirements.txt

2. Установка WebDriver:
Убедитесь, что у вас установлен Chrome и ChromeDriver совместимой версии.

Примечания

Тесты независимы и создают новый экземпляр браузера для каждого теста
Используются явные ожидания (WebDriverWait) для стабильности тестов# Sprint_5
### Last update: Wed Feb  4 14:34:46 MSK 2026
# Sprint_5
# Sprint_5

