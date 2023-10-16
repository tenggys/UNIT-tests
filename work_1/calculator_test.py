import unittest
from calculator import calculateDiscount


class TestCalculator(unittest.TestCase):
    def test_result(self):
        self.assertEqual(90.0, calculateDiscount(purchase_amount=100, discount_amount=10))

    def test_zero_result(self):
        self.assertEqual(0, calculateDiscount(purchase_amount=0, discount_amount=10))

    def test_zero_discount(self):
        self.assertEqual(100, calculateDiscount(purchase_amount=100, discount_amount=0))

    def test_discount_less_0(self):
        self.assertRaisesRegex(ArithmeticError, "Discount can't be less then zero",
                               calculateDiscount, purchase_amount=100, discount_amount=-5)

    def test_discount_more_100(self):
        self.assertRaisesRegex(ArithmeticError, "Discount can't be more then 100",
                               calculateDiscount, purchase_amount=100, discount_amount=110)


if __name__ == '__main__':
    unittest.main(verbosity=2)