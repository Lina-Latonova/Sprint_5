from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators
from .test_data import get_registration_data

def test_login_via_lk_button(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()

    data = get_registration_data()["valid_data"]
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.EMAIL_REG)).send_keys(data["email"])
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_REG)).send_keys(data["password"])
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PROFILE_NAV))
    assert browser.find_element(*Locators.PROFILE_NAV).is_displayed(), "Login failed: Profile button is not visible."

def test_go_to_constructor_by_button(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR)).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Login failed: Constructor button is not visible."

def test_stellarburger(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.STELLAR_BURGERS)).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Login failed: Constructor button is not visible."    