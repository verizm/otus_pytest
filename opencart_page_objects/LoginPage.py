"""
Модуль страницы авторизации
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from opencart_locators import  Login

class LoginPage:
    """
    Класс страницы авторизации
    """
    def __init__(self, driver):
        self.driver = driver

    def input_login(self, value):
        """
        :param value: логин пользователя
        :return: введенное в поле логин значение
        """
        input_login_email = self.driver.find_element_by_css_selector(Login.input_login_email)
        input_login = input_login_email.send_keys(value)
        return input_login

    def input_password(self, value):
        """
        :param value: пароль пользователя
        :return: введенное в поле пароль значение
        """
        input_user_password = self.driver.find_element_by_css_selector(Login.input_login_password)
        input_password = input_user_password.send_keys(value)
        return input_password

    def go_user_account(self):
        """
        Переходит в аккаунт пользователя
        нажатием кнопки
        """
        login_button = self.driver.find_element_by_css_selector(Login.login_button)
        login_button.click()

    def go_main_page(self):
        """
        Возвращает на главную странцу
        """
        wait = WebDriverWait(self.driver, 3)
        continue_button = wait.until(EC.element_to_be_clickable((
            By.PARTIAL_LINK_TEXT, Login.continue_button)))
        continue_button.click()
