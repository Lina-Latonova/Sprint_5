from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators
from .helpers import Helper
from .urls import LOGIN_PAGE_URL

def test_exit(browser):
    # Переходим на страницу регистрации и авторизуемся
    helper = Helper()
    
    browser.get(LOGIN_PAGE_URL)
    helper.login(browser)

    # Открываем профиль
    account_header = browser.find_element(*Locators.ACCOUNT_HEADER)
    account_header.click()

    # Нажимаем кнопку выхода
    wait = WebDriverWait(browser, 10)
    exit_buttons = wait.until(EC.element_to_be_clickable(Locators.EXIT_BUTTON))
    exit_buttons.click()

    # Ждем появления кнопки входа
    wait = WebDriverWait(browser, 10)
    email_field = wait.until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))

    # Финальное утверждение: проверка, что поле ввода электронной почты появилось
    assert email_field.is_displayed(), "Тест провалился: Поле ввода электронной почты не появилось после выхода."
