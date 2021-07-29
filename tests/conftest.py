import pytest as pytest
from selenium import webdriver



@pytest.fixture(autouse=True)
def driver():
    """Setting up browser instance"""

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def context():
    context = {}
    yield context
