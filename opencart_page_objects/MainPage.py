"""
Модуль Главная страница
"""
import time
from opencart_locators import Main

class MainPage:
    """
    Класс главная страница
    """
    class SearchItem:
        """
        Класс продуктов в корзине
        """
        def __init__(self, product):
            self.product = product

        def add_to_cart(self):
            """
            Добавляет товар в корзину
            """
            button = self.product.find_element_by_css_selector(Main.add_to_cart)
            button.click()

        def add_to_wish_list(self):
            """
            Добавляет товар в wish-list
            """
            button = self.product.find_element_by_css_selector(Main.add_to_wish_list)
            button.click()

    def __init__(self, driver):
        self.driver = driver

    def search_products(self, product_name):
        """
        :param product: название продукта
        :return: все отображенные на странице продукты
        """
        field_search = self.driver.find_element_by_css_selector(Main.search_field['css'])
        field_search.send_keys(product_name)
        search_button = self.driver.find_element_by_class_name(Main.input_field)
        search_button.click()

        products = self.driver.find_elements_by_css_selector(Main.products)

        results = []
        for product in products:
            result = MainPage.SearchItem(product)
            results.append(result)
        return results

    def go_shopping_cart_page(self):
        """
        Переход по ссылке в сообщении от системы в корзину
        """
        time.sleep(1)
        alert_href_shopping_cart = self.driver.find_element_by_partial_link_text(
            Main.alert_href_shopping_cart['link_text'])
        alert_href_shopping_cart.click()

    def go_account_page(self):
        """
        Переход на страницу авторизации в лк
        """
        time.sleep(1)
        my_account = self.driver.find_element_by_css_selector(Main.my_account_button)
        my_account.click()
        login_button_dropdown = self.driver.find_element_by_css_selector(
            Main.login_button_locator).find_element_by_partial_link_text(Main.login_button_dropdown)
        login_button_dropdown.click()

    def get_logo_page(self):
        """
        :return: логотип гланой страницы
        """
        main_logo = self.driver.find_element_by_css_selector(Main.main_logo)
        return main_logo
