"""
Модуль содержит класс для перехода
на страницу product
"""

from selenium.webdriver.common.alert import Alert
from opencart_locators import AdminPage, ProductPage, MainPage, FilterPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Utils:

    @staticmethod
    def login_opencart_admin(base_url, driver):
        """
        Вход под учетной записью админа
        :param driver:
        :return:
        """
        driver.get(base_url + "admin/")
        search_input_login = driver.find_element_by_id(AdminPage.admin_login_field)
        search_input_login.send_keys(AdminPage.keys_login)
        search_input_password = driver.find_element_by_id(AdminPage.admint_password_field)
        search_input_password.send_keys(AdminPage.keys_password)
        search_button = driver.find_element_by_class_name(AdminPage.enter_admin_button)
        search_button.click()

    @staticmethod
    def open_prodact_page(driver):
        """
        Переход на страницу продуктов
        :return:
        """
        wait = WebDriverWait(driver, 10)
        search_catalog_button = wait.until(EC.element_to_be_clickable((By.ID, MainPage.catalog_button)))
        search_catalog_button.click()
        search_product_button = driver.find_element_by_partial_link_text(MainPage.product_button)
        search_product_button.click()

    @staticmethod
    def remove_product(driver, product_name):
        form_product = Utils.search_product(driver, product_name)

        tds = form_product.find_elements_by_tag_name(ProductPage.form_product_tag_td)

        for td in tds:
            try:
                test_input = td.find_element_by_tag_name(ProductPage.input_check_in_filter_tag)
                test_input.click()
                button_delete = driver.find_element_by_class_name(ProductPage.delete_button)
                button_delete.click()
                Alert(driver).accept()
            except:
                pass

    @staticmethod
    def add_product(driver, product_name, product_module):
        add_button = driver.find_element_by_css_selector(ProductPage.add_button_div).find_element_by_css_selector(ProductPage.add_button)
        add_button.click()
        input_product_name_field = driver.find_element_by_id(FilterPage.product_name_field) # заполненение полей 1 страница
        input_product_name_field.send_keys(product_name)
        input_meta_title_field = driver.find_element_by_id(FilterPage.meta_title_field)
        input_meta_title_field.send_keys("Meta " + product_name)
        search_data_page = driver.find_element_by_partial_link_text(ProductPage.data_page_link) # заполнение полей 2 страница
        search_data_page.click()
        input_model_field = driver.find_element_by_id(FilterPage.model_field)
        input_model_field.send_keys(product_module)

        search_save_button = driver.find_element_by_css_selector(ProductPage.button_save["css"])
        search_save_button.click() # сохранение

    @staticmethod
    def search_product(driver, product_name):
        search_filter_filed = driver.find_element_by_id(ProductPage.filter_field)
        search_filter_filed.clear()
        search_filter_filed.send_keys(product_name)
        search_filter_button = driver.find_element_by_id(ProductPage.filter_button)
        search_filter_button.click()
        form_product = driver.find_element_by_class_name(ProductPage.form_product_class)
        form_product = form_product.find_element_by_tag_name(ProductPage.form_product_tag)
        return form_product
