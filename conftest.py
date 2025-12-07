import pytest
from selenium import webdriver
from tests.urls import BASE_URL

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver 
    driver.quit()