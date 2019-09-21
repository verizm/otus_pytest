"""
Тесты страницы аккаунт
"""

from opencart_locators import Main, Login, Users, Items, Edit
from opencart_page_objects import MainPage, ShoppingCart,\
    UserAccountPage, LoginPage, AddressPage, AddressChangePage, WishListPage

def test_get_my_account_page(get_parametrize_driver_fixture_page_object):
    """
    Проверяем вход в аккаунт с валидными данными
    зарегистрированного пользователя
    :return:
    """

    driver = get_parametrize_driver_fixture_page_object

    # переход на страницу авторизации (главная страница)
    mainpage = MainPage(driver)
    mainpage.go_account_page()

    # заполнение поля mail пользователя (страница авторизации)
    loginpage = LoginPage(driver)
    loginpage.input_login(Users.user1_mail)

    # заполнение поля пароль пользователя (страница авторизации)
    loginpage.input_password(Users.user1_password)

    # переход в аккаунт пользователя (страница авторизации)
    loginpage.go_user_account()

    # проверяем, что мы на странице аккаунта пользователя (страница аккаунта)
    accountpage = UserAccountPage(driver)
    title_account = accountpage.check_title()
    assert title_account.text == Login.title_account_text

    # выход из аккаунта пользователя (страница аккаунта)
    accountpage.logout()

    # переход на главную страницу (страница авторизации)
    loginpage.go_main_page()

    # проверяем, что мы на главной странице (главная страница)
    main_logo = mainpage.get_logo_page()
    assert main_logo.text == Main.main_logo_text


def test_add_product_shopping_cart(get_parametrize_driver_fixture_page_object):
    """
    Проверяет, добавление товара в корзину
    что поля таблицы корзины содержат валидные данные о товаре
    удаляет продукт из корзины
    :param get_parametrize_driver_fixture_page_object:
    :return:
    """
    driver = get_parametrize_driver_fixture_page_object
    mainpage = MainPage(driver)

    # ищем iphone
    results = mainpage.search_products(Items.product_iphone)

    # добавляем 1й iphone в корзину
    results[0].add_to_cart()

    # переходим в корзину
    mainpage.go_shopping_cart_page()

    shoppingcart = ShoppingCart(driver)

    # получаем список продуктов в корзине
    products = shoppingcart.get_products()

    # проверяем, что в корзине iphone и удаляем его из корзины
    iphone_product = products[0]
    assert iphone_product.get_product_name().text == Items.product_iphone
    assert iphone_product.get_product_model().text == Items.product_iphone_model
    iphone_product.remove()

    # проверяем, что корзина пустая
    assert shoppingcart.check_empty()

    # продолжить шоппинг
    shoppingcart.continue_shopping()


def test_add_product_wish_list(get_parametrize_driver_fixture_page_object):
    """
    Проверяет добавление товара в wish-list
    и наличие данного товара в wish-list
    после входа в аккаунт.
    Удаляет товар из wish-list
    :param get_parametrize_driver_fixture_page_object:
    :return:
    """
    driver = get_parametrize_driver_fixture_page_object
    # поиск iPhone
    mainpage = MainPage(driver)
    results = mainpage.search_products(Items.product_iphone)
    # добавить 1ый iPhone в wish-list (главная страница)
    results[0].add_to_wish_list()

    # перейти на страницу авторизации
    mainpage.go_account_page()

    # перейти в аккаунт пользователя
    loginpage = LoginPage(driver)
    loginpage.input_login(Users.user1_mail)
    loginpage.input_password(Users.user1_password)
    loginpage.go_user_account()

    # перейти на страницу wish-list
    useraccount = UserAccountPage(driver)
    useraccount.go_wish_list()

    # получить список продуктов в wish-list
    wishpage = WishListPage(driver)
    products = wishpage.get_products()

    # проверить, что в wish-list iphone и удалить его из корзины
    iphone_product = products[0]
    iphone_product.remove()
    wishpage.get_alert_message()
    wishpage.continue_shopping()

    # выйти из аккаунта пользователя
    useraccount.logout()


def test_change_user_info(get_parametrize_driver_fixture_page_object):
    """
    Изменяет телефон пользователя в личном кабинете
    :param get_parametrize_driver_fixture_page_object:
    :return:
    """
    driver = get_parametrize_driver_fixture_page_object
    mainpage = MainPage(driver)
    # авторизоваться в аккаунт пользователя
    mainpage.go_account_page()
    loginpage = LoginPage(driver)
    loginpage.input_login(Users.user1_mail)
    loginpage.input_password(Users.user1_password)
    loginpage.go_user_account()

    #перейти на вкладку редактирование аккаунта

    accountpage = UserAccountPage(driver)
    accountpage.go_edit_account()

    # изменить информацию в поле телефон
    accountpage.change_user_phone(Users.phonenamber)

    # нажать продолжить
    accountpage.click_continue()

    # проверить сообщение об успешном изменеии

    # зайти в редактирование
    accountpage.go_edit_account()

    # проверить значение поля телефон
    assert Edit.telephone_field_value

    # выйти из аккаунта
    accountpage.logout()


def test_try_remove_address(get_parametrize_driver_fixture_page_object):
    """
    Проверяет коррестность сообщения от системы
    после попытки удалить карточку с дефолтным адресом
    :param get_parametrize_driver_fixture_page_object:
    :return:
    """
    driver = get_parametrize_driver_fixture_page_object
    # авторизация пользователя в личном кабинете
    mainpage = MainPage(driver)
    mainpage.go_account_page()
    loginpage = LoginPage(driver)
    loginpage.input_login(Users.user1_mail)
    loginpage.input_password(Users.user1_password)
    loginpage.go_user_account()

    #перейти на страницу адресной книги
    accountpage = UserAccountPage(driver)
    accountpage.go_address_book()

    # нажать новый адрес
    addresspage = AddressPage(driver)

    # нажать удалить
    addresses = addresspage.get_addresses()
    default_address = addresses[0]
    default_address.remove()
    # проверить наличие сообщения о
    # том, что нельзя удалить дефолтный адрес
    addresspage.get_message_not_remove()



def test_change_address(get_parametrize_driver_fixture_page_object):
    """
    Изменяет имя и фамилию в карточке дефолтного адреса
    :param get_parametrize_driver_fixture_page_object:
    :return:
    """
    driver = get_parametrize_driver_fixture_page_object
    # авторизация пользователя в личном кабинете
    mainpage = MainPage(driver)
    mainpage.go_account_page()
    loginpage = LoginPage(driver)
    loginpage.input_login(Users.user1_mail)
    loginpage.input_password(Users.user1_password)
    loginpage.go_user_account()
    # перейти на страницу адресной книги
    accountpage = UserAccountPage(driver)
    accountpage.go_address_book()
    # нажать новый адрес
    addresspage = AddressPage(driver)
    # нажать изменить
    addresses = addresspage.get_addresses()
    default_address = addresses[0]
    default_address.edit()
    # изменить значения имени и фамилии
    pagechanger = AddressChangePage(driver)
    pagechanger.set_input_name(Users.name1)
    pagechanger.set_input_lastname(Users.lastname1)
    # сохранить изменеия
    pagechanger.save_changes()
    # получить сообщение о успешном изменении
    addresspage.get_message_change_succes()
