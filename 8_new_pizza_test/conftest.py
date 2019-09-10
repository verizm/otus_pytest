import pytest
from selenium import webdriver


@pytest.fixture()
def get_driver_pizza(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(9)
    driver.maximize_window()
    request.addfinalizer(driver.close)
    return driver
