"""
Модуль для тестирования frontend opencart
"""
from opencart_locators import MainPage, AdminPage, Items

def test_search_iphone(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Проверяем,что при вводе валидного значения товара
    в поле ввода поиск будет осуществлен переход на страницу товара
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_drivers_fixture
    driver.get(get_base_url_fixture)
    search_input = driver.find_element_by_name(MainPage.search_button)
    search_input.send_keys(Items.product_iphone)
    search_button = driver.find_element_by_class_name(MainPage.input_field)
    search_button.click()


def test_open_shopping_cart(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Проверяем переход на страницу shopping_cart
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_drivers_fixture
    driver.get(get_base_url_fixture)
    search_input = driver.find_element_by_xpath(MainPage.shopping_cart_button)
    search_input.click()


def test_open_wish_list(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Проверяем переход на страницу wish_list
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_drivers_fixture
    driver.get(get_base_url_fixture)
    search_button = driver.find_element_by_id(MainPage.wish_list_button)
    search_button.click()


def test_open_about_us(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Проверяем переход на страницу about_us
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_drivers_fixture
    driver.get(get_base_url_fixture)
    search_button = driver.find_element_by_xpath(MainPage.about_us_button)
    search_button.click()


def test_login_admin(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Проверяем вход под учеткой админа с валидными логином и паролем
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_drivers_fixture
    driver.get(get_base_url_fixture + "admin")
    search_input_login = driver.find_element_by_id(AdminPage.admin_login_field)
    search_input_login.send_keys(AdminPage.keys_login)
    search_input_password = driver.find_element_by_id(AdminPage.admint_password_field)
    search_input_password.send_keys(AdminPage.keys_password)
    search_button = driver.find_element_by_class_name(AdminPage.enter_admin_button)
    search_button.click()

    assert AdminPage.main_admin_title in driver.title


def test_get_elements(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Получаем элементы главной страницы с именем клас "container"
    проверяем, что имя класса каждого элемента "container"
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_drivers_fixture
    driver.get(get_base_url_fixture)
    search_elements = driver.find_elements_by_class_name("container")
    assert search_elements
    for element in search_elements:
        assert element.get_attribute('class') == "container"
