import unittest

from geometrylib.circle import Circle


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_area_with_decimal(self):
        circle = Circle(5)
        decimal = 2
        area = circle.area(decimal)
        self.assertAlmostEqual(area, 78.54)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_radius_type(self):
        circle = Circle(5)
        self.assertIsInstance(circle.radius, float)


if __name__ == "__main__":
    unittest.main()
