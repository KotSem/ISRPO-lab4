import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 5)
        self.assertAlmostEqual(res, 0.0)

    def test_normal_area(self):
        res = area(6, 4)
        self.assertAlmostEqual(res, 12.0)

    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_invalid_triangle(self):
        # Треугольник со сторонами 1, 2, 10 существовать не может (1 + 2 < 10)
        res = perimeter(1, 2, 10)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
