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
    
    # Ожидаем появление поля Email и вводим значение
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.EMAIL_FIELD)).send_keys(valid_data["email"])
        
    # Ожидаем поле Password и вводим пароль
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.PASSWORD_FIELD)).send_keys(valid_data["password"])
    
    # Кликаем на кнопку Submit
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)).click()
    
    # Ждем отображения кнопки конструктора
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((Locators.CONSTRUCTOR_BUTTON)))
    
    def scroll_to_element(self, browser, element):
        """Метод для прокрутки к нужному элементу"""
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)    