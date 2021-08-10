to_roman_numerals = input(
    "if you would like to convert TO a roman numeral type Yes, if not type No:\n"
)

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


def convert_arabic_to_roman(digit_list: list) -> str:
    roman_numeral = 0

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

        return roman_numeral

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

        return roman_numeral

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

        print(roman_numeral)

    elif arabic_number_length == 1:

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
        return roman_numeral

    else:
        print("The number must have a minimum of 1 and a maximum of 4 valid digits")
        return None


def convert_roman_to_arabic(digit_list:list) -> int:
    thousands = 0
    hundreds = 0
    tens = 0
    units = 0

    if "MMM" in digit_list[:2]:
        thousands = 3
        digit_list.remove("MMM")

    elif "MM" in digit_list[:1]:
        thousands = 2
        digit_list.remove("MM")

    elif "M" in digit_list[0]:
        thousands = 1
        digit_list.remove("M")

    if "CM" in digit_list:
        hundreds = 9
        digit_list.remove("CM")

    elif "CD" in digit_list:
        hundreds = 4
        digit_list.remove("CD")

    elif "D" in digit_list:
        hundreds = 5
        digit_list.remove("D")

    if "CCC" in digit_list:
        hundreds = 3
        digit_list.remove("CCC")

    elif "CC" in digit_list:

        hundreds = 2
        digit_list.remove("CC")

    elif "C" in digit_list:
        hundreds = 1
        list.remove("C")

    if "XC" in digit_list:
        tens = 9
        digit_list.remove("XC")

    elif "XL" in digit_list:
        tens = 4
        digit_list.remove("XL")

    elif "L" in digit_list:
        tens = 5
        digit_list.remove("L")

    if "XXX" in digit_list:
        tens = 3
        digit_list.remove("XXX")

    elif "XX" in digit_list:
        tens = 2
        digit_list.remove("XX")

    elif "X" in digit_list:
        tens = 1
        digit_list.remove("X")

    if "IX" in digit_list:
        units = 9
        digit_list.remove("IX")

    elif "IV" in digit_list:
        units = 4
        digit_list.remove("IV")

    elif "V" in digit_list:
        units = 5
        digit_list.remove("V")

    if "III" in digit_list:
        units = 3
        digit_list.remove("III")

    elif "II" in digit_list:
        units = 2
        digit_list.remove("II")

    elif "I" in digit_list:
        units = 1
        digit_list.remove("I")

    return (1000 * thousands) + (100 * hundreds) + (10 * tens) + (1 * units)


if to_roman_numerals == "Yes":
    arabic_input = input(
        "Please enter the Arabic number which you want to conver to a Roman Numeral this must between 1 and 3,9,9,9.\n"
    )
    print("The Arabic Number", arabic_input, "will be converted to a Roman Numeral.\n")
    arabic_number_length: int = len(arabic_input)
    print(arabic_number_length)

    digit_list: list = arabic_input.split(",")
    print(digit_list)

    roman_numeral = convert_arabic_to_roman(digit_list)
    print(roman_numeral)

if to_roman_numerals == "No":
    roman_input = input(
        "Please enter the Roman Numeral that you want to convert to an Arabic number with a max of MMM, eg. M,M,C,D,I:\n"
    )
    print("The Roman Numeral", roman_input, "will be converted to an Arabic Number")
    roman_numeral_length = len(roman_input)
    digit_list = roman_input.split(",")
    print(digit_list)
    print("This is the length", roman_numeral_length)  # length includes spaces

    arabic_input: int = convert_roman_to_arabic(digit_list)
    print("the number is: ", arabic_input)

else:
    print("Type yes or no")
