import unittest
from Roman_Number import decimal_to_roman_converter, roman_to_decimal_converter
import os


class RomanTests(unittest.TestCase):
    def test_three(self):
        integer = 3
        roman_number = decimal_to_roman_converter(integer)
        self.assertEqual('III', roman_number)

    def test_four_need_subtract(self):
        integer = 4
        roman_number = decimal_to_roman_converter(integer)
        self.assertEqual('IV', roman_number)

    def test_9(self):
        integer = 9
        roman_number = decimal_to_roman_converter(integer)
        self.assertEqual('IX', roman_number)

    def test_58(self):
        integer = 58
        roman_number = decimal_to_roman_converter(integer)
        self.assertEqual('LVIII', roman_number)

    def test_1994(self):
        integer = 1994
        roman_number = decimal_to_roman_converter(integer)
        self.assertEqual('MCMXCIV', roman_number)

    def test_more_than_3999(self):
        integer = 4500
        roman_number = decimal_to_roman_converter(integer)
        self.assertEqual('MMMMD', roman_number)

# testing convert roman to decimal
    def test_XXXVI(self):
        roman_string = 'XXXVI'
        decimal = roman_to_decimal_converter(roman_string)
        self.assertEqual(36, decimal)

    def test_MMXII(self):
        roman_string = 'MMXII'
        decimal = roman_to_decimal_converter(roman_string)
        self.assertEqual(2012, decimal)

    def test_MCMXCVI(self):
        roman_string = 'MCMXCVI'
        decimal = roman_to_decimal_converter(roman_string)
        self.assertEqual(1996, decimal)

        # Extra tests after version 8: every Roman numeral up to 4999, on a separate line in a text file.
    def test_file(self):
        path = os.path.dirname(__file__) + "/first-4999.txt"
        with open(path) as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                expected = line.strip()
                # creates a test (a "subtest" in Python) for each of them
                # By passing the line number (+1) into the Roman function and checking that the result is the same as the line in the file (which I downloaded from the internet)
                result_to_roman = decimal_to_roman_converter(index + 1)

                with self.subTest():
                    self.assertEqual(result_to_roman, expected)

                result_to_decimal = roman_to_decimal_converter(line)
                with self.subTest():
                    self.assertEqual(result_to_decimal, index + 1)
unittest.main()
