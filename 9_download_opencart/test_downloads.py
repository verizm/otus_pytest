"""
Тест с реализацией загрузки файла
"""

import os
from opencart_page_objects import AdminPage, DownloadsAdmin
from  opencart_locators import AdminMain

def test_download_file(get_options_driver_fixture_admin_page):
    """
    Загрузка файла
    :param get_options_driver_fixture_products_page:
    :return:
    """
    driver = get_options_driver_fixture_admin_page
    adminpage = AdminPage(driver)
    adminpage.get_downloads()

    downloads = DownloadsAdmin(driver)
    downloads.add_new()

    fname = 'CORGI.jpg'
    dirname = os.path.join(os.path.expanduser('~'), 'pictures')
    content_type = 'image/jpeg'
    downloads.upload(fname, dirname, content_type)

    alert = driver.find_element_by_css_selector(AdminMain.alert)
    assert alert.text.split('\n')[0] == "Success: You have modified downloads!"
