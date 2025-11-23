from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_exit(browser):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD)).send_keys("latonova.lina@ya.ru")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD)).send_keys("999999")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.HEADER_LOGIN_BUTTON)).click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON)).click()
      