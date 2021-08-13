

roman_numerals_lookup: dict = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def convert_arabic_to_roman(arabic_input):
    arabic_input = str(arabic_input)
    arabic_number_length: int = len(arabic_input)

    digit_list: list = arabic_input.split(",")
    roman_numeral = ''

    if arabic_number_length == 7:

        if digit_list[0] == "1":
            roman_numeral = "M"

        elif digit_list[0] == "2":
            roman_numeral = "MM"

        elif digit_list[0] == "3":
            roman_numeral = "MMM"

        if digit_list[1] == "1":
            roman_numeral = roman_numeral + "C"

        elif digit_list[1] == "2":
            roman_numeral = roman_numeral + "CC"

        elif digit_list[1] == "3":
            roman_numeral = roman_numeral + "CCC"

        elif digit_list[1] == "4":
            roman_numeral = roman_numeral + "CD"

        elif digit_list[1] == "5":
            roman_numeral = roman_numeral + "D"

        elif digit_list[1] == "9":
            roman_numeral = roman_numeral + "CM"

        if digit_list[2] == "1":
            roman_numeral = roman_numeral + "X"

        elif digit_list[2] == "2":
            roman_numeral = roman_numeral + "XX"

        elif digit_list[2] == "3":
            roman_numeral = roman_numeral + "XXX"

        elif digit_list[2] == "4":
            roman_numeral = roman_numeral + "XL"

        elif digit_list[2] == "5":
            roman_numeral = roman_numeral + "L"

        elif digit_list[2] == "9":
            roman_numeral = roman_numeral + "XC"

        if digit_list[3] == "1":
            roman_numeral = roman_numeral + "I"

        elif digit_list[3] == "2":
            roman_numeral = roman_numeral + "II"

        elif digit_list[3] == "3":
            roman_numeral = roman_numeral + "III"

        elif digit_list[3] == "4":
            roman_numeral = roman_numeral + "IV"

        elif digit_list[3] == "5":
            roman_numeral = roman_numeral + "V"

    elif arabic_number_length == 5:

        if digit_list[0] == "1":
            roman_numeral = "C"

        elif digit_list[0] == "2":
            roman_numeral = "CC"

        elif digit_list[0] == "3":
            roman_numeral = "CCC"

        elif digit_list[0] == "4":
            roman_numeral = "CD"

        elif digit_list[0] == "5":
            roman_numeral = "D"

        elif digit_list[0] == "9":
            roman_numeral = "CM"

        if digit_list[1] == "1":
            roman_numeral = roman_numeral + "X"

        elif digit_list[1] == "2":
            roman_numeral = roman_numeral + "XX"

        elif digit_list[1] == "3":
            roman_numeral = roman_numeral + "XXX"

        elif digit_list[1] == "4":
            roman_numeral = roman_numeral + "XL"

        elif digit_list[1] == "5":
            roman_numeral = roman_numeral + "L"

        elif digit_list[1] == "9":
            roman_numeral = roman_numeral + "XC"

        if digit_list[2] == "1":
            roman_numeral = roman_numeral + "I"

        elif digit_list[2] == "2":
            roman_numeral = roman_numeral + "II"

        elif digit_list[2] == "3":
            roman_numeral = roman_numeral + "III"

        elif digit_list[2] == "4":
            roman_numeral = roman_numeral + "IV"

        elif digit_list[2] == "5":
            roman_numeral = roman_numeral + "V"

    elif arabic_number_length == 3:

        if digit_list[0] == "1":
            roman_numeral = "X"

        elif digit_list[0] == "2":
            roman_numeral = "XX"

        elif digit_list[0] == "3":
            roman_numeral = "XXX"

        elif digit_list[0] == "4":
            roman_numeral = "XL"

        elif digit_list[0] == "5":
            roman_numeral = "L"

        elif digit_list[0] == "9":
            roman_numeral = "XC"

        if digit_list[1] == "1":
            roman_numeral = roman_numeral + "I"

        elif digit_list[1] == "2":
            roman_numeral = roman_numeral + "II"

        elif digit_list[1] == "3":
            roman_numeral = roman_numeral + "III"

        elif digit_list[1] == "4":
            roman_numeral = roman_numeral + "IV"

        elif digit_list[1] == "5":
            roman_numeral = roman_numeral + "V"

    if arabic_number_length == 1:

        if digit_list[0] == "1":
            roman_numeral = "I"

        elif digit_list[0] == "2":
            roman_numeral = "II"

        elif digit_list[0] == "3":
            roman_numeral = "III"

        elif digit_list[0] == "4":
            roman_numeral = "IV"

        elif digit_list[0] == "5":
            roman_numeral = "V"

    else:
        print("The number must have a minimum of 1 and a maximum of 4 valid digits")

    return roman_numeral


def convert_roman_to_arabic(digit_list):
    thousands: int = 0
    hundreds: int = 0
    tens: int = 0
    units: int = 0

    if "MMM" in digit_list[:2]:
        thousands = 3000

    elif "MM" in digit_list[:1]:
        thousands = 2000

    elif "M" in digit_list[0]:
        thousands = 1000

    if "CM" in digit_list:
        hundreds = 900

    elif "CD" in digit_list:
        hundreds = 400

    elif "D" in digit_list:
        hundreds = 500

    elif "CCC" in digit_list:
        hundreds = 300

    elif "CC" in digit_list:

        hundreds = 200

    elif "C" in digit_list:
        hundreds = 100

    if "XC" in digit_list:
        tens = 90

    elif "XL" in digit_list:
        tens = 40

    elif "L" in digit_list:
        tens = 50

    elif "XXX" in digit_list:
        tens = 30

    elif "XX" in digit_list:
        tens = 20

    elif "X" in digit_list:
        tens = 10

    if "IX" in digit_list:
        units = 9

    elif "IV" in digit_list:
        units = 4

    elif "V" in digit_list:
        units = 5

    elif "III" in digit_list:
        units = 3

    elif "II" in digit_list:
        units = 2

    elif "I" in digit_list:
        units = 1

    result = thousands + hundreds + tens + units
    return result


if __name__ == "__main__":
    to_roman_numerals = input(
        "if you would like to convert TO a roman numeral type Yes, if not type No:\n"
    )
    if to_roman_numerals == "Yes":
        arabic_input = input(
            "Please enter the Arabic number which you want to convert to a Roman Numeral this must between 1 and 3,9,9,9.\n"
        )

        print(
            "The Arabic Number", arabic_input, "will be converted to a Roman Numeral.\n"
        )

        roman_numeral = convert_arabic_to_roman(arabic_input)
        print(roman_numeral)

    if to_roman_numerals == "No":
        roman_input = input(
            "Please enter the Roman Numeral which you want to convert to an Arabic Number this must be between I and MMM,CM,XC,IX.\n"
        )
        print("The Roman Numeral", roman_input, "will be converted to an Arabic Number.\n")
        arabic_number_length: int = len(roman_input)
        digit_list: list = roman_input.split(",")
        number = digit_list

        result = convert_roman_to_arabic(digit_list)
        print(result)


    else:
        print("Type yes or no")
