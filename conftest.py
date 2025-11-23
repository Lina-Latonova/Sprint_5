import pytest
import faker
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    yield driver 
    driver.quit()

@pytest.fixture
def generate_test_data():
    fake = faker.Faker('ru_RU')
    return {
        "email": fake.email(),
        "password": fake.password(length=7),
        "name": fake.first_name()
    }