from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators
from .helpers import Helper
from .urls import LOGIN_PAGE_URL

def test_login_from_register(browser):
    helper = Helper()
    browser.get(LOGIN_PAGE_URL)
    helper.login(browser)
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR))
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed()

def test_login_from_main(browser):
    helper = Helper()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    helper.login(browser)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR))
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed()

def test_login_from_header(browser):
    helper = Helper()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()
    helper.login(browser)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR))
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed()    