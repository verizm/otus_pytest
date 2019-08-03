"""Модуль с примерами тестов для определения типа треугольнника"""

from enum import Enum

class Geometry: # pylint: disable=too-few-public-methods
    """Класс для работы с типами треугольников"""

    class TriangleType(Enum):
        """Класс для определения типа треугольника"""
        IS_NOT_TRIANGLE = 1
        EQUILATERAL = 2
        ISOSCELES = 3
        DIFFERENCE = 4

    @staticmethod
    def detect_triangle_type(side_a, side_b, side_c):
        """Метод определяет тип треугольника по соотношению длин"""
        array = sorted([side_a, side_b, side_c])
        if array[0] > 0 and array[0] + array[1] > array[2]:
            if side_a == side_b and side_a == side_c:
                return Geometry.TriangleType.EQUILATERAL

            if side_a == side_b or side_a == side_c or side_b == side_c:
                return Geometry.TriangleType.ISOSCELES

            return Geometry.TriangleType.DIFFERENCE

        return Geometry.TriangleType.IS_NOT_TRIANGLE

def test_equilateral_triangle():
    """Метод проверяет что треугольник равносторонний"""
    for i in range(1, 100):
        assert Geometry.detect_triangle_type(i, i, i) == Geometry.TriangleType.EQUILATERAL

def test_isosceles_triangle():
    """Метод проверяет, что треугольник равнобедренный"""
    assert Geometry.detect_triangle_type(6, 6, 9) == Geometry.TriangleType.ISOSCELES
    assert Geometry.detect_triangle_type(6, 9, 6) == Geometry.TriangleType.ISOSCELES
    assert Geometry.detect_triangle_type(9, 6, 6) == Geometry.TriangleType.ISOSCELES

def test_difference_triangle():
    """Метод проверяет, что треугольник разносторонний"""
    assert Geometry.detect_triangle_type(7, 8, 9) == Geometry.TriangleType.DIFFERENCE
    assert Geometry.detect_triangle_type(8, 9, 7) == Geometry.TriangleType.DIFFERENCE
    assert Geometry.detect_triangle_type(9, 7, 8) == Geometry.TriangleType.DIFFERENCE

def test_zero_notriangle():
    """Метод проверяет, что ни одна из сторон треугольника не равна 0"""
    assert Geometry.detect_triangle_type(0, 0, 0) == Geometry.TriangleType.IS_NOT_TRIANGLE

    assert Geometry.detect_triangle_type(1, 0, 0) == Geometry.TriangleType.IS_NOT_TRIANGLE
    assert Geometry.detect_triangle_type(0, 1, 0) == Geometry.TriangleType.IS_NOT_TRIANGLE
    assert Geometry.detect_triangle_type(0, 0, 1) == Geometry.TriangleType.IS_NOT_TRIANGLE

    assert Geometry.detect_triangle_type(1, 1, 0) == Geometry.TriangleType.IS_NOT_TRIANGLE
    assert Geometry.detect_triangle_type(1, 0, 1) == Geometry.TriangleType.IS_NOT_TRIANGLE
    assert Geometry.detect_triangle_type(0, 1, 1) == Geometry.TriangleType.IS_NOT_TRIANGLE

def test_big_notriangle():
    """Метод проверяет, что фигура является треугольником"""
    assert Geometry.detect_triangle_type(100, 1, 2) == Geometry.TriangleType.IS_NOT_TRIANGLE
    assert Geometry.detect_triangle_type(1, 2, 100) == Geometry.TriangleType.IS_NOT_TRIANGLE
    assert Geometry.detect_triangle_type(2, 100, 1) == Geometry.TriangleType.IS_NOT_TRIANGLE
