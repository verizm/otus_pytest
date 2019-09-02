"""
Модуль содержит тесты, проверяющие функции
создание карточки нового товара
изменение данных о товаре
удаление карточки товара
"""

from opencart_utils import Utils
from opencart_locators import Items, ProductPage


def test_add_product(get_parametrize_driver_fixture_products_page):
    """
    Тест вычищает базу от ранее добавленного продукта
    добавляет продукт
    проверяет, что продукт добавлен
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """

    driver = get_parametrize_driver_fixture_products_page
    Utils.remove_product(driver, Items.product_name_0)

    Utils.open_prodact_page(driver)
    Utils.add_product(driver, Items.product_name_0, Items.product_model_0)

    search_succes_massage = driver.find_element_by_class_name(ProductPage.alert_text)
    assert search_succes_massage  # проверка сохранения


def test_change_product(get_parametrize_driver_fixture_products_page):
    """
    Изменяем поле значение поля quantity
    в карточке товара, сохраняем карточку с новым
    значением, проверяем, что изменение успешно
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_driver_fixture_products_page

    form_product = Utils.search_product(driver, Items.product_iphone)
    tds = form_product.find_elements_by_tag_name(ProductPage.form_product_tag_td)
    td_qty = tds[5]

    qty = int(td_qty.text)
    new_qty = qty + 1

    action_button = tds[7]
    action_button.click()

    data_page = driver.find_element_by_partial_link_text(ProductPage.data_page_link)
    data_page.click()

    product_qty = driver.find_element_by_id(ProductPage.quantity)
    product_qty.clear()
    product_qty.send_keys(new_qty)

    save_button = driver.find_element_by_xpath(ProductPage.button_save)
    save_button.click()

    succes_massage = driver.find_element_by_class_name(ProductPage.alert_text)
    assert succes_massage

    form_product = Utils.search_product(driver, Items.product_iphone)
    tds = form_product.find_elements_by_tag_name(ProductPage.form_product_tag_td)
    td_qty = tds[5]
    check_qty = int(td_qty.text)

    assert check_qty == new_qty


def test_remove_product(get_base_url_fixture, get_parametrize_driver_fixture_products_page):
    """
    Проверяем, что товар присутствует в магазине
    если нет, то создаем карточку нового товара,
    затем удаляем товар.
    Проверяем, что данного товара больше нет в списке.
    :param get_base_url_fixture:
    :param get_options_driver_fixture:
    :return:
    """
    driver = get_parametrize_driver_fixture_products_page
    product_table = Utils.search_product(driver, Items.product_name_1)
    no_result = product_table.find_element_by_class_name(ProductPage.product_table_result_class)
    if no_result.text == ProductPage.result_text:
        Utils.add_product(driver, Items.product_name_1, Items.product_model_1)
        Utils.login_opencart_admin(get_base_url_fixture, driver)
        Utils.open_prodact_page(driver)

    Utils.remove_product(driver, Items.product_name_1)

    search_succes_massage = driver.find_element_by_class_name(ProductPage.alert_text)
    assert search_succes_massage # проверка удаления

    product_table = Utils.search_product(driver, Items.product_name_1)
    no_result = product_table.find_element_by_class_name(ProductPage.product_table_result_class)
    assert no_result.text == ProductPage.result_text