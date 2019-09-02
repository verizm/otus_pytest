"""Модуль с фикстурами"""
import time
import pytest
from selenium import webdriver
from locators_opencart import AdminPage


def pytest_addoption(parser):
    """
    Функция с реализацией базового url opencart
    """
    parser.addoption('--url', action='store', default='http://192.168.122.105/opencart/',
                     help='opencart url')
    parser.addoption('--browser', action='store', default='firefox', help='select browser')


@pytest.fixture()
def get_base_url_fixture(request):
    """
    Фикстура возвращает обьект с конфигурацией
    """
    return request.config.getoption('--url')


def create_driver(request, browser, is_headless=True, sleep_time=0):
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
    return driver


def login_opencart_admin(base_url, driver):
    driver.get(base_url + "admin/")
    search_input_login = driver.find_element_by_id(AdminPage.admin_login_field)
    search_input_login.send_keys(AdminPage.keys_login)
    search_input_password = driver.find_element_by_id(AdminPage.admint_password_field)
    search_input_password.send_keys(AdminPage.keys_password)
    search_button = driver.find_element_by_class_name(AdminPage.enter_admin_button)
    search_button.click()

def get_prodact_page(driver):
    search_catalog_button = driver.find_element_by_id("menu-catalog")
    search_catalog_button.click()
    search_product_button = driver.find_element_by_css("active")


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
def get_options_driver_fixture_admin_page(request):
    """
    Фикстура возвращает драйвер
    """
    browser = request.config.getoption('--browser')
    driver = create_driver(request, browser, False, 5)
    login_opencart_admin(request.config.getoption('--url'), driver)
    search_catalog_button = driver.find_element_by_id("menu-catalog")
    search_catalog_button.click()
    search_product_button = driver.find_element_by_class_name("active")
    search_product_button.click()

    return driver
