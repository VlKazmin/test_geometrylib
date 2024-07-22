from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Метод для расчета площади фигуры. Должен быть реализован в подклассах."""
        pass
