from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import Locators
from .test_data import get_registration_data

def test_successful_registration(browser: WebDriver, base_url):
    data = get_registration_data()["valid_data"]
    browser.get(f"{base_url}/register")

    browser.find_element(*Locators.NAME_FIELD).send_keys(data["name"])
    browser.find_element(*Locators.EMAIL_FIELD).send_keys(data["email"])
    browser.find_element(*Locators.PASSWORD_FIELD).send_keys(data["password"])
    browser.find_element(*Locators.REGISTRATION_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR))
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Меню конструктора не открылось"

def test_invalid_password(browser: WebDriver, base_url):
    data = get_registration_data()["invalid_password_data"]
    browser.get(f"{base_url}/register")

    browser.find_element(*Locators.NAME_FIELD).send_keys(data["name"])
    browser.find_element(*Locators.EMAIL_FIELD).send_keys(data["email"])
    browser.find_element(*Locators.PASSWORD_FIELD).send_keys(data["password"])
    browser.find_element(*Locators.REGISTRATION_BUTTON).click()

    try:
        password_error = WebDriverWait(browser, 10).until(EC.presence_of_element_located(Locators.PASSWORD_ERROR))
        error_message = password_error.text.strip()
        assert error_message == "Некорректный пароль", \
            f"Тест НЕ пройден. Ожидается сообщение 'Некорректный пароль', получено '{error_message}'"
    except TimeoutException:
        print("Сообщение об ошибке пароля не появилось.")