from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .test_locators import Locators
from selenium.webdriver.common.by import By
import time

class TestConstructorPage:

    def scroll_to_element(self, browser, element):
        """Метод для прокрутки к нужному элементу"""
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def test_go_to_filling(self, browser):
        """Проверка перехода в раздел 'Начинки'."""
        filling_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.FILLING_BUTTON))
        self.scroll_to_element(browser, filling_button)
        filling_button.click()
        filling_header_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.FILLING_HEADER))
        assert filling_header_element.text == 'Начинки', "Заголовок 'Начинки' не отображается или текст не соответствует."

    def test_go_to_bread(self, browser): # тоже не работает
        """Проверка перехода в раздел 'Булки'."""
        bread_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.BREAD_BUTTON))
        self.scroll_to_element(browser, bread_button)
        
        # Поиск элемента и клик через JavaScript
        element = browser.find_element(By.CSS_SELECTOR, Locators.BREAD_BUTTON)
        browser.execute_script("arguments[0].click();", element)
        
        bread_header_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BREAD_HEADER))
        assert bread_header_element.is_displayed(), "Заголовок 'Булки' не отображается"
        assert bread_header_element.text == 'Булки', "Текст заголовка не совпадает с ожидаемым значением"
        

    def test_go_to_sauce(self, browser): # последняя версия
        """Проверка перехода в раздел 'Соусы'."""
        # Дождёмся полной загрузки страницы
        WebDriverWait(browser, 10).until(lambda x: x.execute_script("return document.readyState") == "complete")

        # Исключение проверки AJAX-запросов
        # WebDriverWait(browser, 10).until(lambda x: x.execute_script("return window.jQuery && jQuery.active === 0"))

        # Ищем элемент
        sauce_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.SAUCE_BUTTON))

        # Прокручиваем элемент в центр окна
        self.scroll_to_element(browser, sauce_button)

        # Подтверждаем, что элемент кликабелен
        sauce_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(sauce_button))

        # Клик по элементу
        sauce_button.click()

        # Паузу оставляем небольшой
        time.sleep(2)

        # Проверяем наличие заголовка "Соусы"
        sauce_header = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.SAUCE_HEADER))
        assert sauce_header.text == 'Соусы', "Заголовок 'Соусы' не отображается или текст не соответствует."
