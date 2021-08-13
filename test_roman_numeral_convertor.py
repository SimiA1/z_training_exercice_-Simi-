import unittest
import roman_numeral_convertor

# checking from arabic to roman conversions


class RomanNumeralConvertorTest(unittest.TestCase):
    def test_simple_conversion(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(1)
        expected_value = "I"
        self.assertEqual(key_value, expected_value)

    def test_complicated_conversion(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(1, 2, 3)
        expected_value = "CXXIII"
        self.assertEqual(key_value, expected_value)

    def test_simple_subtraction(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(4)
        expected_value = "IV"
        self.assertEqual(key_value, expected_value)

    def test_complex_subtraction(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(900)
        expected_value = "CM"
        self.assertEqual(key_value, expected_value)

    def test_long_converison(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(3, 9, 9, 9)
        expected_value = "MMMCMXCIX"
        self.assertEqual(key_value, expected_value)


# checking from roman to arabic conversion


class NumeralRomanConvertorTest(unittest.TestCase):
    def test_simple_conversion(self):
        key_value = roman_numeral_convertor.convert_roman_to_arabic("I")
        expected_value = 1
        self.assertEqual(key_value, expected_value)

    def test_complicated_conversion(self):
        key_value = roman_numeral_convertor.convert_roman_to_arabic("C,XX,III")
        expected_value = 123
        self.assertEqual(key_value, expected_value)

    def test_simple_subtraction(self):
        key_value = roman_numeral_convertor.convert_roman_to_arabic("IV")
        expected_value = 4
        self.assertEqual(key_value, expected_value)

    def test_complex_subtraction(self):
        key_value = roman_numeral_convertor.convert_roman_to_arabic("CM")
        expected_value = 900
        self.assertEqual(key_value, expected_value)

    def test_long_converison(self):
        key_value = roman_numeral_convertor.convert_roman_to_arabic("MMM,CM,XC,IX")
        expected_value = 3999
        self.assertEqual(key_value, expected_value)
