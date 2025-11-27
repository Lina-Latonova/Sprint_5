from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .test_locators import Locators
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

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
    error_message = browser.find_element(*Locators.ERROR_MESSAGE).text
    assert error_message == "Не корректный пароль"\
        f"Тест НЕ пройден. Ожидается сообщение 'Не корректный пароль', получено '{error_message}'"