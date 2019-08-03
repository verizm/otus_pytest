"""Модуль содержит фикстуры"""
import string
import pytest

@pytest.fixture
def function_fixture(request):
    """Фикстура function"""
    print(f'\n[F] Initialize fixture {request.scope}')

    def fin():
        print(f"\n[F] Finelize from {request.scope}")
    request.addfinalizer(fin)

@pytest.fixture(scope="class")
def class_fixture(request):
    """Фикстура class"""
    print(f"\n[C] Initialize fixture {request.scope}")

    def fin():
        print(f"\n[C] Finelize from {request.scope}")

    request.addfinalizer(fin)

@pytest.fixture(scope="module")
def module_fixture(request):
    """Фикстура module"""
    print(f"\n[M] Initialize fixture {request.scope}")

    def fin():
        print(f"\n[M] Finelize from {request.scope}")

    request.addfinalizer(fin)

@pytest.fixture(scope="session")
def session_fixture(request):
    """Фикстура session"""
    print(f"\n[S] Initialize fixture {request.scope}")

    def fin():
        print(f"\n[S] Finelize from {request.scope}")

    request.addfinalizer(fin)

@pytest.fixture(scope="function")
def month_fixture():
    """Фикстура возвращает список с месяцами года"""
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    return months

@pytest.fixture(scope="class")
def string_fixture():
    """Фикстура возвращает строку с латинским алфавитом в нижнем регистре"""
    ascii_str = string.ascii_lowercase
    return ascii_str

@pytest.fixture(scope="class")
def dict_fixture():
    """Фикструра возвращает словарь"""
    my_dict = {1: 'q', 2: 'w', 3: 'r'}
    return my_dict
