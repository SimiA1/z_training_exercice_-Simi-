import unittest
import roman_numeral_convertor

# checking from arabic to roman conversions


class check_roman_numeral_convertor(unittest.TestCase):
    def simple_conversion(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(1)
        expected_value = "I"
        self.assertEqual(key_value, expected_value)

    def complicated_conversion(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(1, 2, 3)
        expected_value = "CXXIII"
        self.assertEqual(key_value, expected_value)

    def simple_subtraction(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(4)
        expected_value = "IV"
        self.assertEqual(key_value, expected_value)

    def complex_subtraction(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(900)
        expected_value = "CM"
        self.assertEqual(key_value, expected_value)

    def long_converson(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman(3, 9, 9, 9)
        expected_value = "MMMCMXCIX"
        self.assertEqual(key_value, expected_value)


if __name__ == "__main__":
    unittest.main()


# checking from roman to arabic conversion


class check_roman_numeral_convertor(unittest.TestCase):
    def simple_conversion(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman("I")
        expected_value = 1
        self.assertEqual(key_value, expected_value)

    def complicated_conversion(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman("C,XX,III")
        expected_value = 123
        self.assertEqual(key_value, expected_value)

    def simple_subtraction(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman("IV")
        expected_value = 4
        self.assertEqual(key_value, expected_value)

    def complex_subtraction(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman("CM")
        expected_value = 900
        self.assertEqual(key_value, expected_value)

    def long_converson(self):
        key_value = roman_numeral_convertor.convert_arabic_to_roman("MMM,CM,XC,IX")
        expected_value = 3999
        self.assertEqual(key_value, expected_value)


if __name__ == "__main__":
    unittest.main()
