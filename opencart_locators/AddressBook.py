"""
Класс адресная книга
"""

class AdderssBook:
    """
    содержит локаторы
    для работы с адресной книгой
    """
    #кнопка новый адрес
    new_address = "div"
    # элементы таблицы с адресом
    table = " div#content div.table-responsive"
    tbody = "tbody"
    tr = "tr"
    td = "td.text-right"
    edit_button = "Edit"
    remove_button = "Delete"
    # элементы таблицы с инфо адреса создание изменение
    div_content = "div#content"
    div_field = "input"
    field_name = "input-firstname"
    field_lastname = "input-lastname"
    # выбор региона
    div_content = "div#content"
    div = "div:nth-of-type(9) select[name='zone_id']"
    option_zone = "Kaluga"
    # выбор страны
    div_content = "div#content"
    div = "div:nth-of-type(8)"
    option_country = "Russion Federation"
    # кнопка сохранить изменеия (continue)
    div = "div.buttons"
    continue_button = "input[value='Continue']"
    # элементы для сообщений от системы
    alert_messge = "div.alert"
    text_remove = "Warning: You must have at least one address!"
    text_change = "Your address has been successfully updated"
