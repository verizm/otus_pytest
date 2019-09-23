"""
Модуль главной страницы админки
"""
from opencart_locators import AdminMain

class AdminPage:
    """
    Класс главной страницы админки
    """
    def __init__(self, driver):
        self.driver = driver

    def get_downloads(self):
        """
        Переход на страницу загрузок
        :return:
        """
        nav_catalog = self.driver.find_element_by_css_selector(
            AdminMain.nav_catalog["css"])
        catalog_button = nav_catalog.find_element_by_css_selector(
            AdminMain.catalog_button["css"])
        catalog_button.click()

        all_pages_catalog = self.driver.find_element_by_css_selector(
            AdminMain.all_pages_catalog["css"])
        download_button = all_pages_catalog.find_element_by_partial_link_text(
            AdminMain.download_button["partial_link"])
        download_button.click()
