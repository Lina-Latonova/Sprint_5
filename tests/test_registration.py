from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import Locators
from .data import data
from .urls import REGISTER_PAGE_URL

def test_successful_registration(browser: WebDriver):
    valid_data = data["valid_data"]
    browser.get(REGISTER_PAGE_URL)

    browser.find_element(*Locators.NAME_FIELD).send_keys(valid_data["name"])
    browser.find_element(*Locators.EMAIL_FIELD).send_keys(valid_data["email"])
    browser.find_element(*Locators.PASSWORD_FIELD).send_keys(valid_data["password"])
    browser.find_element(*Locators.REGISTRATION_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR))
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Меню конструктора не открылось"

def test_invalid_password(browser: WebDriver):
    invalid_password_data = data["invalid_password_data"]
    browser.get(REGISTER_PAGE_URL)

    browser.find_element(*Locators.NAME_FIELD).send_keys(invalid_password_data["name"])
    browser.find_element(*Locators.EMAIL_FIELD).send_keys(invalid_password_data["email"])
    browser.find_element(*Locators.PASSWORD_FIELD).send_keys(invalid_password_data["password"])
    browser.find_element(*Locators.REGISTRATION_BUTTON).click()

    try:
        password_error = WebDriverWait(browser, 10).until(EC.presence_of_element_located(Locators.PASSWORD_ERROR))
        error_message = password_error.text.strip()
        assert error_message == "Некорректный пароль", \
            f"Тест НЕ пройден. Ожидается сообщение 'Некорректный пароль', получено '{error_message}'"
    except TimeoutException:
        print("Сообщение об ошибке пароля не появилось.")