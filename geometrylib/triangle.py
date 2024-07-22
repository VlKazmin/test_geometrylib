from math import sqrt, isclose

from dataclasses import dataclass

from geometrylib.shape import Shape


@dataclass
class Triangle(Shape):
    """
    Класс для представления треугольника.

    Attributes:
        a (int): Длина первой стороны треугольника. Должна быть положительным числом.
        b (int): Длина второй стороны треугольника. Должна быть положительным числом.
        c (int): Длина третьей стороны треугольника. Должна быть положительным числом.
    """

    a: int
    b: int
    c: int

    def __post_init__(self):

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            """Проверяет, что стороны треугольника положительные и удовлетворяют неравенству треугольника."""

            raise ValueError("Стороны треугольника должны быть положительными.")

        if (
            (self.a + self.b <= self.c)
            or (self.a + self.c <= self.b)
            or (self.b + self.c <= self.a)
        ):
            raise ValueError(
                "Сумма любых двух сторон должна быть больше третьей стороны."
            )

    def area(self, decimal=None):
        """
        Рассчитывает площадь треугольника по формуле Герона.

        Args:
            decimal (int, optional): Число знаков после запятой для округления результата.

        Returns:
            float: Площадь треугольника.
        """

        s = (self.a + self.b + self.c) / 2
        area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        if decimal is None:
            return area
        return round(area, decimal)

    def is_right_angled(self):
        """
        Проверяет, является ли треугольник прямоугольным по теореме Пифагора.

        Returns:
            bool: True, если треугольник прямоугольный, иначе False.
        """

        sides = sorted([self.a, self.b, self.c])
        return isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
