"""
Модуль Корзина
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from opencart_locators import Main, Login, Items

class ShoppingCart:
    """
    Класс страницы Корзина
    """
    class ShoppingCartItem:
        """
        Класс продуктов в корзине
        """
        def __init__(self, itr):
            self.itr = itr

        def get_product_name(self):
            """
            :return: возвращает имя продукта
            """
            product_name = self.itr.find_element_by_css_selector(Items.product_name)
            return product_name

        def get_product_model(self):
            """
            :return: возвращаем модель продукта
            """
            product_model = self.itr.find_element_by_css_selector(Items.product_model)
            return product_model

        def remove(self):
            """
            Удаляет элемент из корзины
            """
            remove_product_shopping_cart = self.itr.find_element_by_css_selector(
                Main.remove_product_shopping_cart)
            remove_product_shopping_cart.click()

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        """
        :return: Возвращает списко продуктов в корзине
        """
        table_response = self.driver.find_element_by_css_selector(Main.table_response)
        tbody = table_response.find_element_by_tag_name(Main.tbody)
        trs = tbody.find_elements_by_tag_name("tr")
        products = []
        for itr in trs:
            product = ShoppingCart.ShoppingCartItem(itr)
            products.append(product)
        return products

    def check_empty(self):
        """
        Проверяет что корзина пустая
        """
        time.sleep(1)
        remove_product_message = self.driver.find_element_by_css_selector(
            Main.remove_product_message)
        return remove_product_message.text == Main.remove_product_message_text

    def continue_shopping(self):
        """
        Продолжить шоппинг
        """
        wait = WebDriverWait(self.driver, 3)
        continue_button = wait.until(EC.element_to_be_clickable((
            By.PARTIAL_LINK_TEXT, Login.continue_button)))
        continue_button.click()
