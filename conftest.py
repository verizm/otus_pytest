"""Модуль с фикстурами"""

import os
import time
import logging
from datetime import date

import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from opencart_utils import Utils

def pytest_addoption(parser):
    """
    Функция с реализацией базового url opencart
    """
    parser.addoption('--url', action='store', default='http://192.168.88.215/',
                     help='opencart url')
    parser.addoption('--browser', action='store', default='firefox', help='select browser')
    parser.addoption('--implicitly_delay', action='store',
                     default=0, help='set time for implicity_wait')
    parser.addoption('--manual_delay', action='store',
                     default=12, help='set time for WebDriverWait()')


@pytest.fixture()
def get_base_url_fixture(request):
    """
    Фикстура возвращает базовый URL opencart
    """
    return request.config.getoption('--url')


@pytest.fixture()
def get_manual_delay_fixture(request):
    """
    Фикстура задержку для ручного ожидания
    """
    return request.config.getoption('--manual_delay')


def build_logger(logdir, datestr):
    """
    Вспомогательный метод для создания логгера
    :return:
    """
    # Create a custom logger
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(os.path.join(logdir, "selenium_" + datestr + '.log'))

    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(asctime)s : %(filename)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s : %(filename)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


class MyListener(AbstractEventListener):
    """
    Мой лисенер логов
    """
    def __init__(self, logger, logdir, datestr):
        self.logger = logger
        self.logdir = logdir
        self.datestr = datestr

    def before_find(self, by, value, driver):
        self.logger.info('before_find:' + "'" + by + "' " + "'" + value + "'")

    def after_find(self, by, value, driver):
        self.logger.info('after_find: ' + "'" + by + "' " + "'" + value + "'")

    def before_navigate_to(self, url, driver):
        self.logger.info('before_navigate:' + "'" + url + "'")

    def after_navigate_to(self, url, driver):
        self.logger.info('after_navigate: ' + "'" + url + "'")

    def on_exception(self, exception, driver):
        self.logger.error("on_exception: " + str(exception))
        # get PATH for  get test name
        tlist = os.environ.get('PYTEST_CURRENT_TEST').split('/')
        # format test name
        testname = tlist[len(tlist) - 1]
        testname = testname.replace(" (call)", "")
        # create name of screen
        fname = "selenium_" + testname + "_" + self.datestr + ".png"
        # create path for
        fpath = os.path.join(self.logdir, fname)
        # save screen
        self.logger.error("saving screen: " + fpath)
        driver.save_screenshot(fpath)


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
    logdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    datestr = str(date.today())

    driver = None
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if is_headless:
            options.add_argument('--headless')
        gekolog = os.path.join(logdir, "geckodriver.log")
        driver = webdriver.Firefox(options=options, service_log_path=gekolog)
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

    # maximize browser window
    driver.maximize_window()

    # setup optional implicitly_wait
    delay = request.config.getoption('--implicitly_delay')
    if int(delay) > 0:
        driver.implicitly_wait(delay)

    listener = MyListener(build_logger(logdir, datestr), logdir, datestr)
    ew_driver = EventFiringWebDriver(driver, listener)

    def finalizer():
        time.sleep(sleep_time)
        driver.close()

    request.addfinalizer(finalizer)

    return ew_driver


@pytest.fixture
def get_options_driver_fixture(request):
    """
    Фикстура для ручного тестирования
    Возвращает драйвер
    Открывает браузер на весь экран
    Ждет 5 секунд после окончания теста
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
    return create_driver(request, browser_param, False, 1)


@pytest.fixture
def get_options_driver_fixture_products_page(request):
    """
    Фикстура логинится в админку
    переходит на страницу продуктов
    """
    browser = request.config.getoption('--browser')
    manual_delay = request.config.getoption('--manual_delay')
    driver = create_driver(request, browser, False, 5)
    Utils.login_opencart_admin(request.config.getoption('--url'), driver)
    Utils.open_prodact_page(driver, manual_delay)
    return driver


@pytest.fixture(params=["firefox"])
def get_parametrize_driver_fixture_products_page(request):
    """
    Фикстура позволяет проводить тесты админки
    в заданных браузерах
    :param request:
    :return:
    """
    manual_delay = request.config.getoption('--manual_delay')
    browser_param = request.param
    driver = create_driver(request, browser_param)
    Utils.login_opencart_admin(request.config.getoption('--url'), driver)
    Utils.open_prodact_page(driver, manual_delay)
    return driver


@pytest.fixture(params=["chrome", "firefox"])
def get_parametrize_driver_fixture_page_object(request):
    """
    Фикстура для тестов в патерне page object
    :param request:
    :return: возвращает драйвер
    """
    browser_param = request.param
    driver = create_driver(request, browser_param)
    driver.implicitly_wait(9)
    driver.get(request.config.getoption('--url'))
    return driver


@pytest.fixture(params=["chrome", "firefox"])
def get_options_driver_fixture_admin_page(request):
    """
    Фикстура логинится в админку
    """
    browser = request.config.getoption('--browser')
    driver = create_driver(request, browser)
    Utils.login_opencart_admin(request.config.getoption('--url'), driver)
    driver.implicitly_wait(8)
    return driver

@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request):
    """
    Фикстура с расширениями для html report
    """
    # получаем путь к текущему файлу - он лежит в корне проекта
    projectdir = os.path.dirname(__file__)
    file = open(os.path.join(projectdir, 'requirements.txt'))
    request.config._metadata.update( # pylint: disable=W0212
        {
            "driver": request.config.getoption("--browser"),
            "url": request.config.getoption("--url"),
            "implicitly_delay": request.config.getoption("--implicitly_delay"),
            "manual_delay": request.config.getoption("--manual_delay"),
            "path": os.environ["PATH"],
            "lc_name": os.environ["LC_NAME"],
            "requirements": file.readlines()
        }
    )
    yield
