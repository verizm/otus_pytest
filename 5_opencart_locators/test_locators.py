"""
Модуль для тестирования frontend opencart
"""
from opencart_locators import Main, Admin, Items
from opencart_utils import Utils

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
    search_input = driver.find_element_by_css_selector(Main.search_field['css'])
    search_input.send_keys(Items.product_iphone)
    search_button = driver.find_element_by_class_name(Main.input_field)
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
    div = driver.find_element_by_css_selector(Main.shopping_cart_button_div)
    search_input = div.find_element_by_css_selector(Main.shopping_cart_button)
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
    search_button = driver.find_element_by_css_selector(Main.wish_list_button)
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
    search_button = driver.find_element_by_partial_link_text(Main.about_us_button)
    search_button.click()


def test_login_admin(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Проверяем вход под учеткой админа с валидными логином и паролем
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_drivers_fixture
    Utils.login_opencart_admin(get_base_url_fixture, driver)

    assert Admin.main_admin_title in driver.title


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
