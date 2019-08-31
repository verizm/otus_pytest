"""Модуль для запуска тестов opencart"""

def test_opencart(get_base_url_fixture, get_parametrize_drivers_fixture):
    """
    Проверяем заголовок на главной странице opencart
    """
    driver = get_parametrize_drivers_fixture
    driver.get(get_base_url_fixture)
    assert "Your Store" in driver.title
