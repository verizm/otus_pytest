"""Модуль с фикстурами"""
import time
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """
    Функция с реализацией базового url opencart
    """
    parser.addoption('--url', action='store', default='http://192.168.88.209/opencart/',
                     help='opencart url')
    parser.addoption('--browser', action='store', default='firefox', help='select browser')

@pytest.fixture()
def get_base_url_fixture(request):
    """
    Фикстура возвращает обьект с конфигурацией
    """
    return request.config.getoption('--url')

@pytest.fixture
def get_driver_fixture(request):
    """
    Фикстура возвращает драйвер
    """
    browser = request.config.getoption('--browser')
    driver = None
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser == 'ie':
        options = webdriver.IeOptions()
        options.add_argument('--headless')
        driver = webdriver.Ie(options=options)
    else:
        raise ValueError('Unsupported browser. Please select from [firefox, ie, chrome]')

    def finalizer():
        time.sleep(3)
        driver.close()

    request.addfinalizer(finalizer)
    return driver
