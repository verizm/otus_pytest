"""
Класс главной страницы
"""

class Main:
    """
    содержит элементы главной страницы
    """
    # тайтл главной страницы
    input_field = "input-group-btn"
    main_logo = "div#logo a"
    main_logo_text = "Your Store"
    # поле поиска
    search_field = {"css": "input[placeholder='Search']"}
    shopping_cart_button_div = "div#top-links"
    shopping_cart_button = "li a[title='Shopping Cart']"
    products = "div.product-grid" # найденные продукты
    # кнопки nav
    wish_list_div = "div#top-links li:nth-of-type(3)"
    wish_list_button = "li:nth-of-type(3) a"  #виш-лист #wishlist-total
    #кнопки footer
    about_us_button = "About Us"
    catalog_button = "menu-catalog"
    product_button = "Products"
    # локаторы "My Account"
    my_account_button = "div#top-links a[title='My Account']"
    login_button_locator = "ul.dropdown-menu-right"
    login_button_dropdown = "Login"
    # локаторы Корзины
    add_to_cart = "div.button-group button:nth-of-type(1)"
    # локаторы wish-list
    add_to_wish_list = "div.button-group button:nth-of-type(2)"
    # ccылка на корзину в сообщении
    alert_href_shopping_cart = {"link_text": "shopping cart"}
    # локаторы для таблицы товара в Корзине
    table_response = "div.table-responsive"
    tbody = "tbody"

    # кнопка удаления товара в таблице Корзины
    remove_product_shopping_cart = "td button[data-original-title='Remove']"
    remove_product_message = "div#content p"
    remove_product_message_text = "Your shopping cart is empty!"
