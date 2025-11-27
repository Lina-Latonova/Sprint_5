from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .test_locators import Locators
from .test_data import get_registration_data

def login(browser):
    data = get_registration_data()["valid_data"]
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD)).send_keys(data["email"])
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD)).send_keys(data["password"])
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))

    assert browser.find_element(*Locators.BUTTON_CONSTRUCTOR).is_displayed(), "Login failed: Constructor button is not visible."

def test_login_from_main(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    login(browser)

def test_login_from_header(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()
    login(browser)

def test_login_from_register(browser, base_url):
    browser.get(f"{base_url}/register")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.ACCOUNT_LINK)).click()
    login(browser)
