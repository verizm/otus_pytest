"""
Модуль с фикстурами
"""

import pytest
from selenium import webdriver

@pytest.fixture(params=["firefox", "chrome"])
def get_driver_drag_n_drop(request):
    """
    Фикстура для создания драйвера
    :param request:
    :return:
    """
    driver = None
    if request.param == "firefox":
        driver = webdriver.Firefox()
    if request.param == "chrome":
        driver = webdriver.Chrome()
    driver.implicitly_wait(9)  # seconds
    driver.maximize_window()
    request.addfinalizer(driver.close)
    return driver
