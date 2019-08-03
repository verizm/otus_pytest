"""Модуль содержит тесты на основные операции с базовыми типами данных"""
import string

class TestList:
    """Класс содержит методы для проверки списков"""
    def test_size(self, month_fixture):
        """Метод класса TestList проверяет, что количество месяцев равно 12 """
        assert self
        assert len(month_fixture) == 12

    def test_append(self, month_fixture):
        """Метод класса TestList проверяет, что посде добавление в список одного элемента,
         количество элементов стало  13"""
        assert self
        month_fixture.append("None")
        assert len(month_fixture) == 13

    def test_copy_method(self, month_fixture):
        """Метод класса TestList проверяет, что количество индексов элементов списка
         равно количеству элементов списка"""
        assert self
        month_fixture_copy = month_fixture.copy()
        for i, item in enumerate(month_fixture):
            assert month_fixture_copy[i] == item

    def test_copy_slice(self, month_fixture):
        """Метод класса TestList проверяет, что количество индексов элементов списка
         равно количеству элементов списка"""
        assert self
        month_fixture_copy = month_fixture[:]
        for i, item in enumerate(month_fixture):
            assert month_fixture_copy[i] == item

    def test_clear(self, month_fixture):
        """Метод класса TestList проверяет, что после удаления содержимого списка,
         в списке нет элементов"""
        assert self
        month_fixture.clear()
        assert month_fixture == []

class TestString:
    """Класс содержит методы для проверки строк"""
    def test_isalpha(self, string_fixture):
        """Метод класса TestString проверяет, что символы строки - буквы"""
        assert self
        assert string_fixture.isalpha()

    def test_concatenation(self, string_fixture):
        """"Метод класса TestString проверяет, что при слоежении списка и результата выполнения
         метода .upper модуля string получится результат выполнения
          метода .ascii_letters модуля string"""
        assert self
        alfabet = string_fixture[:]
        assert alfabet + alfabet.upper() == string.ascii_letters

class TestDict:
    """Класс содержит методы для проверки словарей"""

    def test_get_value(self, dict_fixture):
        """Метод класса TestDict проверяет, что значение словаря полученное по ключу (1) равно q"""
        assert self
        assert dict_fixture.get(1) == 'q'

    def test_keys(self, dict_fixture):
        """Метод класса TestDict проверяет, что словарь содержит ключи [1, 2, 3]"""
        assert self
        assert list(dict_fixture.keys()) == [1, 2, 3]
