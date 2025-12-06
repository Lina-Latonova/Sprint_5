from .locators import Locators
from .helpers import Helper

class TestConstructorPage:
    def test_go_to_bread(self, browser):
        # Прокручиваем страницу к кнопке "Булки" и производим проверку сразу в утверждении
        helper = Helper()
        bread_button = browser.find_element(*Locators.BREAD_BUTTON)
        helper.scroll_to_element(browser, bread_button)
       
        browser.execute_script("arguments[0].click();", bread_button) # проходит только с JavaScript-клик

        # Оставляем поиск элемента только в утверждении
        assert browser.find_element(*Locators.selected_button).text == "Булки", "Активна не кнопка 'Булки'"

    def test_go_to_sauce(self, browser):
        # Ждем доступности кнопки "Соусы" и прокручиваем страницу к ней
        helper = Helper()
        sauce_button = browser.find_element(*Locators.SAUCE_BUTTON)
        helper.scroll_to_element(browser, sauce_button)
        sauce_button.click()

        # Проверяем, что активна именно кнопка "Соусы"
        assert browser.find_element(*Locators.selected_button).text == "Соусы", "Активна не кнопка 'Соусы'"

    def test_go_to_filling(self, browser):
        # Ждем доступности кнопки "Начинки" и прокручиваем страницу к ней
        helper = Helper()
        filling_button = browser.find_element(*Locators.FILLING_BUTTON)
        helper.scroll_to_element(browser, filling_button)
        filling_button.click()

        # Проверяем, что активна именно кнопка "Начинки"
        assert browser.find_element(*Locators.selected_button).text == "Начинки", "Активна не кнопка 'Начинки'"