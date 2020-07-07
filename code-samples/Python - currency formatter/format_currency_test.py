import unittest
from format_currency import format_currency

class CurrencyTest(unittest.TestCase):
    def test_zero(self):
        results = format_currency(0)
        self.assertEqual("0.00", results)

    def test_two_digit_after_point(self):
        results = format_currency(123456.78)
        self.assertEqual("123,456.78", results)

    def test_round_three_digit_after_point(self):
        results = format_currency(123456.786)
        self.assertEqual("123,456.79", results)

    def test_comma_in_integer(self):
        results = format_currency(123456)
        self.assertEqual("123,456.00", results)

    def test_less_than_three_digit(self):
        results = format_currency(12)
        self.assertEqual("12.00", results)

    def test_four_digits(self):
        results = format_currency(1234)
        self.assertEqual("1,234.00", results)

    def test_fewer_than_two_digits_after_point(self):
        results = format_currency(1.5)
        self.assertEqual("1.50", results)

    def test_rounding(self):
        results = format_currency(1.0059)
        self.assertEqual("1.01", results)

unittest.main()