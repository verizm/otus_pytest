"""
Класс редактирование информации аккаунта
"""

class Edit:
    """
    содержит локаторы
    страницы редактирования информации аккаунта
    пользователя
    """
    # поле телефон
    telephone_tag = "div#content div:nth-of-type(4)"
    telephone_field = "input#input-telephone"
    telephone_field_value = "input#input-telephone[value='+72222222']"
    # кнопка продолжить
    continue_button = "input[value='Continue']"
