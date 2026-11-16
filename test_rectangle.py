import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(5, 4), 20)

    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 4), 18)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5, 4)

    def test_float_area(self):
        self.assertEqual(area(2.5, 4), 10.0)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(5, -4)

    def test_area_both_zero(self):
        self.assertEqual(area(0, 0), 0)

    def test_perimeter_both_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_area_first_zero(self):
        self.assertEqual(area(0, 5), 0)

    def test_perimeter_first_zero(self):
        self.assertEqual(perimeter(0, 5), 10)

    def test_area_second_zero(self):
        self.assertEqual(area(5, 0), 0)

    def test_perimeter_second_zero(self):
        self.assertEqual(perimeter(5, 0), 10)

    def test_area_reversed_sides(self):
        self.assertEqual(area(4, 5), 20)

    def test_perimeter_reversed_sides(self):
        self.assertEqual(perimeter(4, 5), 18)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_float(self):
        self.assertEqual(perimeter(2.5, 4), 13.0)

    def test_area_small_fraction(self):
        self.assertEqual(area(0.5, 0.5), 0.25)

    def test_perimeter_small_fraction(self):
        self.assertEqual(perimeter(0.5, 0.5), 2.0)

    def test_area_large(self):
        self.assertEqual(area(1_000_000, 1_000_000), 1_000_000_000_000)

    def test_perimeter_large(self):
        self.assertEqual(perimeter(1_000_000, 1_000_000), 4_000_000)

    def test_area_negative_second(self):
        with self.assertRaises(ValueError):
            area(5, -4)

    def test_perimeter_negative_first(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 4)

    def test_area_both_negative(self):
        with self.assertRaises(ValueError):
            area(-5, -4)

    def test_perimeter_both_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5, -4)

    def test_area_negative_with_zero(self):
        with self.assertRaises(ValueError):
            area(-1, 0)

    def test_perimeter_negative_with_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0, -1)

    def test_area_fraction_precision(self):
        self.assertAlmostEqual(area(0.1, 0.2), 0.02)

    def test_perimeter_fraction_precision(self):
        self.assertAlmostEqual(perimeter(0.1, 0.2), 0.6)

    def test_area_unit_square(self):
        self.assertEqual(area(1, 1), 1)