"""
Модуль содержит класс для перехода
на страницу product
"""

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from opencart_locators import Admin, Product, Filter, Main

class Utils:
    """
    Класс с набором утилит для тестов
    """

    @staticmethod
    def login_opencart_admin(base_url, driver):
        """
        Вход под учетной записью админа
        :param driver:
        :return:
        """
        driver.get(base_url + "admin/")
        search_input_login = driver.find_element_by_id(Admin.admin_login_field)
        search_input_login.send_keys(Admin.keys_login)
        search_input_password = driver.find_element_by_id(Admin.admint_password_field)
        search_input_password.send_keys(Admin.keys_password)
        search_button = driver.find_element_by_class_name(Admin.enter_admin_button)
        search_button.click()

    @staticmethod
    def open_prodact_page(driver, manual_delay):
        """
        Переход на страницу продуктов
        :return:
        """
        wait = WebDriverWait(driver, manual_delay)
        search_catalog_button = wait.until(
            EC.element_to_be_clickable((By.ID, Main.catalog_button)))
        search_catalog_button.click()
        wait1 = WebDriverWait(driver, manual_delay)
        search_product_button = wait1.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, Main.product_button)))

        search_product_button.click()

    @staticmethod
    def remove_product(driver, product_name):
        """
        Удаляем продутк
        :param driver:
        :param product_name:
        :return:
        """
        form_product = Utils.search_product(driver, product_name)

        tds = form_product.find_elements_by_tag_name(Product.form_product_tag_td)

        for td in tds:
            try:
                test_input = td.find_element_by_tag_name(Product.input_check_in_filter_tag)
                test_input.click()
                button_delete = driver.find_element_by_class_name(Product.delete_button)
                button_delete.click()
                Alert(driver).accept()
            except NoSuchElementException:
                pass

    @staticmethod
    def add_product(driver, product_name, product_module, manual_delay):
        """
        Добавляем продукт
        :param driver:
        :param product_name:
        :param product_module:
        :param manual_delay:
        :return:
        """
        div_with_buttons = driver.find_element_by_css_selector(Product.add_button_div)
        add_button = div_with_buttons.find_element_by_css_selector(Product.add_button)
        add_button.click()

        # заполненение полей 1 страница
        input_product_name_field = driver.find_element_by_id(Filter.product_name_field)
        input_product_name_field.send_keys(product_name)
        input_meta_title_field = driver.find_element_by_id(Filter.meta_title_field)
        input_meta_title_field.send_keys("Meta " + product_name)
        wait = WebDriverWait(driver, manual_delay)

        # заполнение полей 2 страница
        search_data_page = wait.until(EC.presence_of_element_located(
            (By.PARTIAL_LINK_TEXT, Product.data_page)))
        search_data_page.click()

        input_model_field = driver.find_element_by_id(Filter.model_field)
        input_model_field.send_keys(product_module)

        # сохранение
        search_save_button = driver.find_element_by_css_selector(Product.button_save["css"])
        search_save_button.click()

    @staticmethod
    def search_product(driver, product_name):
        """
        Ищем продукт
        :param driver:
        :param product_name:
        :return:
        """
        search_filter_filed = driver.find_element_by_id(Product.filter_field)
        search_filter_filed.clear()
        search_filter_filed.send_keys(product_name)
        search_filter_button = driver.find_element_by_id(Product.filter_button)
        search_filter_button.click()
        form_product = driver.find_element_by_class_name(Product.form_product_class)
        form_product = form_product.find_element_by_tag_name(Product.form_product_tag)
        return form_product

    @staticmethod
    def get_wait_timeout():
        """
        Таймаут по умолчанию
        :return:
        """
        return 9
