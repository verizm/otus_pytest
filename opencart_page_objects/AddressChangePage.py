"""
Модуль страницы измения или создания адреса
"""
from opencart_locators import AdderssBook


class AddressChangePage:
    """
    Класс страницы измения или создания адреса
    """
    def __init__(self, driver):
        self.driver = driver

    def set_input_name(self, name):
        """
        Изменяет имя
        :param name: новое значение имени
        """
        field_name = self.driver.find_element_by_id(AdderssBook.field_name)
        field_name.clear()
        field_name.send_keys(name)

    def set_input_lastname(self, lastname):
        """
        Изменяет фамилию
        :param lastname: новое значение фамилии
        """
        field_lastname = self.driver.find_element_by_id(AdderssBook.field_lastname)
        field_lastname.clear()
        field_lastname.send_keys(lastname)

    def save_changes(self):
        """
        Сохраняет изменения
        """
        div = self.driver.find_element_by_css_selector(AdderssBook.div)
        continue_button = div.find_element_by_css_selector(AdderssBook.continue_button)
        continue_button.click()
