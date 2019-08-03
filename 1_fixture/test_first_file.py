"""Модуль с примерами тестов функций и класса с использоанием фикстур разных типов:
session, module, function, class.
Предназначен для ручного запуска тестов и изучения работы фикстур"""

def test_all_fixture_example_1(class_fixture, function_fixture, module_fixture, session_fixture):
    """Метод проверяет уровни фикстур"""
    print(f"\n[T] Start case 1 function:",
          class_fixture, function_fixture, module_fixture, session_fixture)
    assert True

def test_all_fixture_example_2(function_fixture, class_fixture, module_fixture, session_fixture):
    """Метод проверяет работу фикстур"""
    print(f"\n[T] Start case 2 function:",
          class_fixture, function_fixture, module_fixture, session_fixture)
    assert True

class TestAllFixture:
    """Класс содержит методы проверяющие рабоу фикстур уровня класса"""

    def test_method_all_fixture_example_3(self, class_fixture, function_fixture,
                                          module_fixture, session_fixture):
        """Метод проверяет работу фикстур уровня класса"""
        print(f"\n[T] Start case 3 function:",
              class_fixture, function_fixture, module_fixture, session_fixture)
        assert self

    def test_method_all_fixture_example_4(self, function_fixture, class_fixture,
                                          module_fixture, session_fixture):
        """Метод проверяет работу фикстур уровня класса"""
        print(f"\n[T] Start case 4 function:",
              class_fixture, function_fixture, module_fixture, session_fixture)
        assert self
