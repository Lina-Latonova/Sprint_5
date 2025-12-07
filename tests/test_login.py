from .locators import Locators
from .helpers import Helper
from .urls import LOGIN_PAGE_URL

def test_login_from_register(browser):
    helper = Helper()
    browser.get(LOGIN_PAGE_URL)
    helper.login(browser)
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Кнопка конструктора не отображается после входа через регистрацию"

def test_login_from_main(browser):
    helper = Helper()
    browser.find_element(*Locators.LOGIN_BUTTON).click()
    helper.login(browser)
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Кнопка конструктора не отображается после входа с главной страницы."

def test_login_from_header(browser):
    helper = Helper()
    browser.find_element(*Locators.HEADER_LOGIN_BUTTON).click()
    helper.login(browser)
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Кнопка конструктора не отображается после входа через шапку сайта."
   