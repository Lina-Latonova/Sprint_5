from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from locators import Locators

def test_constructor(browser):
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.FILLING_BUTTON)).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.FILLING_HEADER))

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.SAUCE_BUTTON)).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.SAUCE_HEADER))

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.BREAD_BUTTON)).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BREAD_HEADER))
