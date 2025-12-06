from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators
from .data import data


class Helper:
    def login(self, browser):
        """
        Выполняет вход пользователя с использованием валидных учетных данных.
        :param browser: Объект браузера Selenium
        """
        valid_data = data["valid_data"]
    
    # Просто находим и вводим данные, без ожидания
        email_field = browser.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys(valid_data["email"])

        password_field = browser.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(valid_data["password"])

    # Сразу кликаем на кнопку входа
        submit_button = browser.find_element(*Locators.SUBMIT_BUTTON)
        submit_button.click()
    
    def registration_valid(self, browser):
        valid_data = data["valid_data"]
        
    # Просто находим и вводим данные, без ожидания
        name_field = browser.find_element(*Locators.NAME_FIELD)
        name_field.send_keys(valid_data["name"])
        
        email_field = browser.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys(valid_data["email"])

        password_field = browser.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(valid_data["password"])

    # Сразу кликаем на кнопку входа
        registration_button = browser.find_element(*Locators.REGISTRATION_BUTTON)
        registration_button.click()

    def registration_invalid(self, browser):
        invalid_data = data["invalid_data"]
        
    # Просто находим и вводим данные, без ожидания
        name_field = browser.find_element(*Locators.NAME_FIELD)
        name_field.send_keys(invalid_data["name"])
        
        email_field = browser.find_element(*Locators.EMAIL_FIELD)
        email_field.send_keys(invalid_data["email"])

        password_field = browser.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys(invalid_data["password"])

    # Сразу кликаем на кнопку входа
        registration_button = browser.find_element(*Locators.REGISTRATION_BUTTON)
        registration_button.click()    

    def scroll_to_element(self, browser, element):
        """Метод для прокрутки к нужному элементу"""
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)    