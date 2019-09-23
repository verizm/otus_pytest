"""
Модуль главной страницы админки
"""

class AdminMain:
    """
    Класс с элементами главной страницы
    админки
    """
    # каталог
    nav_catalog = {'css': 'nav#column-left'}
    catalog_button = {'css': 'li#menu-catalog'}
    # кнопка загрузки в каталоге
    all_pages_catalog = {'css': 'ul#collapse1'}
    download_button = {'partial_link': 'Downloads'}
    # кнопка добавить новое
    add_button_div = "div.pull-right"
    add_button = ("a[data-original-title='Add New']")
    button_save = {"css": "button[data-original-title='Save']"}
    alert = "div.alert"
    field_mask = {'id': 'input-mask'}
    field_name = {"css": "input[placeholder='Download Name']"}
