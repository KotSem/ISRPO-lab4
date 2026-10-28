import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)


if __name__ == '__main__':
    unittest.main()
