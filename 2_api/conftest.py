"""Модуль содержит фикстуры и функции с реализацией параметров"""
import pytest

def pytest_addoption(parser):
    """Функция с реализацией параметра url
    """
    parser.addoption('--url', action='store', default='https://ya.ru', help='website url')

@pytest.fixture()
def get_config(request):
    """Фикстура возвращает обьект
    с конфигурацией"""
    return request.config
