"""Модуль для запуска тестов opencart"""

def test_opencart(get_base_url_fixture, get_driver_fixture):
    """
    Проверяем заголовок на главной странице opencart
    """
    driver = get_driver_fixture
    driver.get(get_base_url_fixture)
    assert "Your Store" in driver.title
