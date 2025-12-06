from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators
from .data import data
from tests.urls import BASE_URL
from .helpers import Helper

def test_login_via_lk_button(browser):
    helper = Helper()
    browser.get(BASE_URL)
    browser.find_element(*Locators.HEADER_LOGIN_BUTTON).click()
    helper.login(browser)
    browser.find_element(*Locators.HEADER_LOGIN_BUTTON).click()
    
    wait = WebDriverWait(browser, 10) # без него не работает
    profile_nav = wait.until(EC.visibility_of_element_located(Locators.PROFILE_NAV))

    assert profile_nav.is_displayed(), "Login failed: Profile button is not visible."

def test_go_to_constructor_by_button(browser):
    browser.get(BASE_URL)
    browser.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
    assert browser.find_element(*Locators.CONSTRUCTOR_BUTTON).is_displayed()

def test_stellarburger(browser):
    browser.get(BASE_URL)
    browser.find_element(*Locators.STELLAR_BURGERS).click()
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed()