import unittest

from geometrylib.triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_area_with_decimal(self):
        triangle = Triangle(3, 4, 5)
        decimal = 2
        area = triangle.area(decimal)
        self.assertAlmostEqual(area, 6)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_sides_type(self):
        triangle = Triangle(3, 4, 5)
        self.assertIsInstance(triangle.a, int)
        self.assertIsInstance(triangle.b, int)
        self.assertIsInstance(triangle.c, int)

    def test_triangle_is_right_angled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())


if __name__ == "__main__":
    unittest.main()
