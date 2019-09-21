"""
Модуль главной страницы
личного кабинета пользователя
"""

from opencart_locators import Login, Main, Account, Edit

class UserAccountPage:
    """
    Класс главной страницы
    личного кабинета пользователя
    """
    def __init__(self, driver):
        self.driver = driver

    def check_title(self):
        """
        :return: заголовок страницы аккаунта
        """
        title_account = self.driver.find_element_by_css_selector(Login.title_account)
        return title_account

    def logout(self):
        """
        Выход из аккаунта
        """
        my_account = self.driver.find_element_by_css_selector(Main.my_account_button)
        my_account.click()
        logout_button = self.driver.find_element_by_partial_link_text(Login.logout_button)
        logout_button.click()

    def go_edit_account(self):
        """
        Переход на страницу редактирования данных
        """
        edit_div = self.driver.find_element_by_css_selector(Account.editdiv)
        edit_button = edit_div.find_element_by_partial_link_text(Account.edit_button)
        edit_button.click()

    def change_user_phone(self, value):
        """
        :param value: номер телефона
        :return: новый номер телефона пользователя
        """
        telephone_tag = self.driver.find_element_by_css_selector(Edit.telephone_tag)
        telephone_field = telephone_tag.find_element_by_css_selector(Edit.telephone_field)
        telephone_field.clear()
        new_phone = telephone_field.send_keys(value)
        return  new_phone

    def click_continue(self):
        """
        :return: кнопку сохранить и продолжить
        """
        continue_button = self.driver.find_element_by_css_selector(Edit.continue_button)
        return continue_button

    def go_wish_list(self):
        """
        Переход на страницу wish-list
        """
        wish_div = self.driver.find_element_by_css_selector(Account.wish_div)
        wish_button = wish_div.find_element_by_partial_link_text(Account.wish_button)
        wish_button.click()

    def go_address_book(self):
        """
        Переход на страницу аддресоной книги
        """
        adderss_div = self.driver.find_element_by_css_selector(Account.address_div)
        address_button = adderss_div.find_element_by_partial_link_text(Account.address_button)
        address_button.click()
