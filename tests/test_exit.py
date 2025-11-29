from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .test_locators import Locators
from .test_data import get_registration_data
from selenium.common.exceptions import TimeoutException

def test_exit(browser, base_url):
    # Получаем данные для регистрации из файла test_data.py
    data = get_registration_data()["valid_data"]

    # Кликаем на кнопку логина в хедере
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()

    # Вводим email и пароль в поля
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD)).send_keys(data["email"])
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD)).send_keys(data["password"])

    # Подтверждаем вход
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)).click()

    # Проверяем, что пользователь вошел в систему (отображается кнопка в хедере)
    logged_in_constructor = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.HEADER_LOGIN_BUTTON))
    assert logged_in_constructor.is_displayed(), "Пользователь не вошел в систему"

    # Кликаем на кнопку профиля для вызова меню
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()

    # Кликаем на кнопку выхода
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON)).click()

    # Проверяем, что произошел выход из системы. Часто после выхода должна быть видна кнопка логина.
    # Если вместо sauce header появляется кнопка логина, то стоит заменить SAUCE_HEADER на логатор HEADER_LOGIN_BUTTON
    try:
        logout_screen = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.HEADER_LOGIN_BUTTON))
        assert logout_screen.is_displayed(), "Пользователь не вышел из системы"
    except TimeoutException:
        #Если кнопка не появилась за 10 секунд - тест упадет
        assert False, "Элемент не появился после выхода"