"""
Модуль для тестирования code.makery
"""
from selenium.webdriver.common.action_chains import ActionChains

def test_drag_n_drop(get_driver_drag_n_drop):
    """
    Перетаскиваем элементы в корзину
    :param get_driver_drag_n_drop:
    :return:
    """
    driver = get_driver_drag_n_drop
    driver.get("https://marcojakob.github.io/dart-dnd/custom_avatar/")
    trash = driver.find_element_by_class_name("trash")
    iframe = driver.find_elements_by_tag_name("img")
    for element in iframe:
        action = ActionChains(driver).drag_and_drop(element, trash)
        action.perform()
