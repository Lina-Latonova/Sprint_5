from selenium.webdriver.chrome.webdriver import WebDriver
from .locators import Locators
from .urls import REGISTER_PAGE_URL
from .helpers import Helper

def test_successful_registration(browser: WebDriver):
    helper = Helper()
    browser.get(REGISTER_PAGE_URL)
    helper.registration_valid(browser)

    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Меню конструктора не открылось"

def test_invalid_password(browser: WebDriver):
    helper = Helper()
    browser.get(REGISTER_PAGE_URL)
    helper.registration_invalid(browser)
    
    assert browser.find_element(*Locators.PASSWORD_ERROR).text.strip() == "Некорректный пароль", "Сообщение об ошибке пароля неправильное"