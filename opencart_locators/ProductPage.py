"""
Класс содержит элементы для работы с карточкой товара
"""
class ProductPage:
    """
    Элементы product page
    Элементы таблицы товара
    """
    filter_field = "input-name"
    filter_button = "button-filter"
    quantity = "input-quantity"
    product_table_result_class = "text-center"
    form_product_class = "table-bordered" # элементы для таблицы
    form_product_tag = "tbody"
    form_product_tag_td = "td"
    input_check_in_filter_tag = "input" # элементы для чекбокса
    input_check_in_filter_atr_name = "name"
    filter_atr_value_for_name = "selected[]"
    delete_button = "btn-danger" # кнопка удалить
    data_page_link = "Data" # переход на вкладку дата
    all_button_tag = "button"
    button_save_atr = "data-original-title"
    button_save_atr_name = "Save"
    with_buttons = "pull-right"
    add_button = "/html/body/div/div/div[1]/div/div/a"
    button_save = "/html/body/div[1]/div/div[1]/div/div/button"
    alert_text = "alert-success"
    result_text = "No results!"