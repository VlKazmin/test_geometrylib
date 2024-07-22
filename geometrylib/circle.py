from math import pi

from dataclasses import dataclass, field

from geometrylib.shape import Shape


@dataclass
class Circle(Shape):
    """
    Класс для представления окружности.

    Attributes:
        radius (float): Радиус окружности. Должен быть положительным числом.
    """

    radius: float = field(default=0.0)

    def __post_init__(self):
        """Проверяет, что радиус не является отрицательным."""

        if self.radius < 0:
            raise ValueError("Радиус не может быть меньше 0")
        self.radius = float(self.radius)

    def area(self, decimal=None):
        """
        Рассчитывает площадь окружности.

        Args:
            decimal (int, optional): Число знаков после запятой для округления результата.

        Returns:
            float: Площадь окружности.
        """

        area = pi * (self.radius**2)
        if decimal is None:
            return area

        return round(area, decimal)
