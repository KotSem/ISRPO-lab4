import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25, places=5)

    def test_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5, places=5)


if __name__ == '__main__':
    unittest.main()
