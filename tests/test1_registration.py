from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_successful_registration(browser, generate_test_data):
    browser.get("https://stellarburgers.education-services.ru/register")

    browser.find_element(*Locators.NAME_FIELD).send_keys("Лина_Латонова_33_999@ya.ru")
    browser.find_element(*Locators.EMAIL_FIELD).send_keys("latonova.lina@ya.ru")
    browser.find_element(*Locators.PASSWORD_FIELD).send_keys("999999")
    browser.find_element(*Locators.SUBMIT_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BUTTON_CONSTRUCTOR))

def test_invalid_password(browser, generate_test_data):
    browser.get("https://stellarburgers.education-services.ru/register")
    test_data = generate_test_data
    browser.find_element(*Locators.NAME_FIELD).send_keys(test_data["name"])
    browser.find_element(*Locators.EMAIL_FIELD).send_keys(test_data["email"])
    browser.find_element(*Locators.PASSWORD_FIELD).send_keys("123")
    browser.find_element(*Locators.SUBMIT_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
    error_message = browser.find_element(*Locators.PASSWORD_ERROR).text
    assert error_message == "Не корректный пароль"
