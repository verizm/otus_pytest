"""
Модуль адресная страница
"""
import time
from opencart_locators import AdderssBook

class AddressPage:
    """
    Класс адресная страница
    """
    class AddresesCart:
        """
        Класс карточка адреса
        """
        def __init__(self, itr):
            self.itr = itr

        def remove(self):
            """
            Удаляет карточку с адресом
            """
            time.sleep(1)
            remove_td = self.itr.find_element_by_css_selector(AdderssBook.td)
            remove_button = remove_td.find_element_by_partial_link_text(AdderssBook.remove_button)
            remove_button.click()

        def edit(self):
            """
            Переход на страницу карточки адреса
            для внесения изменений
            """
            edit_button = self.itr.find_element_by_partial_link_text(AdderssBook.edit_button)
            edit_button.click()


    def __init__(self, driver):
        self.driver = driver

    def new_address_click(self):
        """
        Переход на страницу создания нового адреса
        """
        new_adderss_button = self.driver.find_element_by_css_selector(AdderssBook.new_address)
        new_adderss_button.click()

    def get_addresses(self):
        """
        :return: все карточки с адресами
        """
        time.sleep(1)
        table_response = self.driver.find_element_by_css_selector(AdderssBook.table)
        tbody = table_response.find_element_by_tag_name(AdderssBook.tbody)
        trs = tbody.find_elements_by_tag_name(AdderssBook.tr)
        addreses = []
        for itr in trs:
            addres = AddressPage.AddresesCart(itr)
            addreses.append(addres)
        return addreses

    def get_message_not_remove(self):
        """
        Проверяет сообщение от системы
        при попытки удалить дефолтый адрес
        """
        alert_messge = self.driver.find_element_by_css_selector(AdderssBook.alert_messge)
        text = alert_messge.text
        assert text == AdderssBook.text_remove

    def get_message_change_succes(self):
        """
        Проверяет сообщение от системы
        после изменеия данных адреса
        """
        alert_messge = self.driver.find_element_by_css_selector(AdderssBook.alert_messge)
        text = alert_messge.text
        assert text == AdderssBook.text_change
