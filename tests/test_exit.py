from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .test_locators import Locators
from .test_data import get_registration_data

def test_exit(browser, base_url):
    data = get_registration_data()["valid_data"]
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD)).send_keys(data["email"])
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD)).send_keys(data["password"])
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)).click()
   
    logged_in_constructor = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.HEADER_LOGIN_BUTTON))
    assert logged_in_constructor.is_displayed(), "Пользователь не вошел в систему"
   
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON)).click()
      
    logout_screen = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.SAUCE_HEADER))
    assert logout_screen.is_displayed(), "Пользователь не вышел из системы"