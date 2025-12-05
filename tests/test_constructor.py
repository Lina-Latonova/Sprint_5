from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators
import time
from .helpers import Helper

class TestConstructorPage:
    def test_go_to_bread(self, browser):
        # Ждём доступность кнопки "Булки" и прокручиваем страницу к ней
        helper = Helper()
        bread_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.BREAD_BUTTON))
        helper.scroll_to_element(browser, bread_button)
        #time.sleep(1)  # Дожидаемся полной готовности элемента
        browser.execute_script("arguments[0].click();", bread_button)

        # Проверяем, что активна именно кнопка "Булки"
        selected_button_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.selected_button)).text
        assert selected_button_text == "Булки"

    def test_go_to_sauce(self, browser):
        # Ждем доступности кнопки "Соусы" и прокручиваем страницу к ней
        helper = Helper()
        sauce_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.SAUCE_BUTTON))
        helper.scroll_to_element(browser, sauce_button)
        sauce_button.click()

        # Проверяем, что активна именно кнопка "Соусы"
        selected_button_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.selected_button)).text
        assert selected_button_text == "Соусы"

    def test_go_to_filling(self, browser):
        # Ждем доступности кнопки "Начинки" и прокручиваем страницу к ней
        helper = Helper()
        filling_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(Locators.FILLING_BUTTON))
        helper.scroll_to_element(browser, filling_button)
        filling_button.click()

        # Проверяем, что активна именно кнопка "Начинки"
        selected_button_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.selected_button)).text
        assert selected_button_text == "Начинки"