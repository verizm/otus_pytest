"""Модуль с фикстурами"""

import time
import pytest
from selenium import webdriver
from opencart_utils import Utils


def pytest_addoption(parser):
    """
    Функция с реализацией базового url opencart
    """
    parser.addoption('--url', action='store', default='http://192.168.88.215/',
                     help='opencart url')
    parser.addoption('--browser', action='store', default='firefox', help='select browser')
    parser.addoption('--delay', action='store', default=0, help='select time for implicity_wait' )

@pytest.fixture()
def get_base_url_fixture(request):
    """
    Фикстура возвращает обьект с конфигурацией
    """
    return request.config.getoption('--url')


def create_driver(request, browser, is_headless=True, sleep_time=0):
    """
    Вспомогательная функция для
    инициализации драйвера
    :param request:
    :param browser:
    :param is_headless:
    :param sleep_time:
    :return:
    """
    driver = None
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if is_headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        if is_headless:
            options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser == 'ie':
        options = webdriver.IeOptions()
        if is_headless:
            options.add_argument('--headless')
        driver = webdriver.Ie(options=options)
    else:
        raise ValueError('Unsupported browser. Please select from [firefox, ie, chrome]')

    def finalizer():
        time.sleep(sleep_time)
        driver.close()

    request.addfinalizer(finalizer)

    delay = request.config.getoption('--delay')
    if delay > 0:
        driver.implicitly_wait(delay)

    driver.maximize_window()

    return driver


@pytest.fixture
def get_options_driver_fixture(request):
    """
    Фикстура возвращает драйвер
    """
    browser = request.config.getoption('--browser')
    return create_driver(request, browser, False, 5)


@pytest.fixture(params=["chrome", "firefox"])
def get_parametrize_drivers_fixture(request):
    """
    Фикстура позволяет проводить тесты
    в заданных браузерах
    :param request:
    :return:
    """
    browser_param = request.param
    return create_driver(request, browser_param)


@pytest.fixture
def get_options_driver_fixture_products_page(request):
    """
    Фикстура возвращает драйвер
    """
    browser = request.config.getoption('--browser')
    driver = create_driver(request, browser, False, 5)
    Utils.login_opencart_admin(request.config.getoption('--url'), driver)
    Utils.open_prodact_page(driver)
    return driver


@pytest.fixture(params=["firefox"])
def get_parametrize_driver_fixture_products_page(request):
    """
    Фикстура позволяет проводить тесты
    в заданных браузерах
    :param request:
    :return:
    """
    browser_param = request.param
    driver = create_driver(request, browser_param)
    Utils.login_opencart_admin(request.config.getoption('--url'), driver)
    Utils.open_prodact_page(driver)
    return driver
