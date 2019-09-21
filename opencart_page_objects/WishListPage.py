"""
Класс страницы Wish-List
"""

from opencart_locators import WishList, Login

class WishListPage:
    """
    Страница wish-list
    """
    class WishListItem:
        """
        Продукты в wish-list
        """
        def __init__(self, itr):
            self.itr = itr

        def remove(self):
            """
            Удалить элемент
            """
            remove_button = self.itr.find_element_by_css_selector(WishList.remove_button)
            remove_button.click()

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        """
        Получить список продуктов
        """
        table_response = self.driver.find_element_by_css_selector(WishList.table_response)
        tbody = table_response.find_element_by_tag_name(WishList.tbody)
        trs = tbody.find_elements_by_tag_name(WishList.tr)
        products = []
        for itr in trs:
            product = WishListPage.WishListItem(itr)
            products.append(product)
        return products

    def continue_shopping(self):
        """
        Продолжить шоппинг
        """
        continue_button = self.driver.find_element_by_partial_link_text(Login.continue_button)
        continue_button.click()


    def get_alert_message(self):
        """
        Получить текст алертов
        """
        alert_messge = self.driver.find_element_by_css_selector(WishList.alert_messge)
        text = alert_messge.text
        assert text
