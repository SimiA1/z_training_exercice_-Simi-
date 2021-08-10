to_roman_numerals = input(
    "if you would like to convert TO a roman numeral type Yes, if not type No:\n"
)

Roman_Numerals = {
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

if to_roman_numerals == "Yes":
    Arabic = input(
        "Please enter the Arabic number which you want to conver to a Roman Numeral this must between 1 and 3,9,9,9.\n"
    )
    print("The Arabic Number", Arabic, "will be converted to a Roman Numeral.\n")
    Arabic_length = len(Arabic)
    print(Arabic_length)
    List = Arabic.split(",")
    print(List)

    def Arabic_to_Roman():
        Numeral = 0
        TH = 0
        HU = 0
        TE = 0
        UN = 0
        seven = 0
        five = 0
        three = 0
        one = 0
        count = 0
        Found = True
        Z = 0

        if Arabic_length == 7:

            if List[0] == "1":
                Numeral = "M"

            elif List[0] == "2":
                Numeral = "MM"

            elif List[0] == "3":
                Numeral = "MMM"

            if List[1] == "1":
                Numeral = Numeral + "C"

            elif List[1] == "2":
                Numeral = Numeral + "CC"

            elif List[1] == "3":
                Numeral = Numeral + "CCC"

            elif List[1] == "4":
                Numeral = Numeral + "CD"

            elif List[1] == "5":
                Numeral = Numeral + "D"

            elif List[1] == "9":
                Numeral = Numeral + "CM"

            if List[2] == "1":
                Numeral = Numeral + "X"

            elif List[2] == "2":
                Numeral = Numeral + "XX"

            elif List[2] == "3":
                Numeral = Numeral + "XXX"

            elif List[2] == "4":
                Numeral = Numeral + "XL"

            elif List[2] == "5":
                Numeral = Numeral + "L"

            elif List[2] == "9":
                Numeral = Numeral + "XC"

            if List[3] == "1":
                Numeral = Numeral + "I"

            elif List[3] == "2":
                Numeral = Numeral + "II"

            elif List[3] == "3":
                Numeral = Numeral + "III"

            elif List[3] == "4":
                Numeral = Numeral + "IV"

            elif List[3] == "5":
                Numeral = Numeral + "V"

            print(Numeral)

        elif Arabic_length == 5:

            if List[0] == "1":
                Numeral = "C"

            elif List[0] == "2":
                Numeral = "CC"

            elif List[0] == "3":
                Numeral = "CCC"

            elif List[0] == "4":
                Numeral = "CD"

            elif List[0] == "5":
                Numeral = "D"

            elif List[0] == "9":
                Numeral = "CM"

            if List[1] == "1":
                Numeral = Numeral + "X"

            elif List[1] == "2":
                Numeral = Numeral + "XX"

            elif List[1] == "3":
                Numeral = Numeral + "XXX"

            elif List[1] == "4":
                Numeral = Numeral + "XL"

            elif List[1] == "5":
                Numeral = Numeral + "L"

            elif List[1] == "9":
                Numeral = Numeral + "XC"

            if List[2] == "1":
                Numeral = Numeral + "I"

            elif List[2] == "2":
                Numeral = Numeral + "II"

            elif List[2] == "3":
                Numeral = Numeral + "III"

            elif List[2] == "4":
                Numeral = Numeral + "IV"

            elif List[2] == "5":
                Numeral = Numeral + "V"

            print(Numeral)

        elif Arabic_length == 3:

            if List[0] == "1":
                Numeral = "X"

            elif List[0] == "2":
                Numeral = "XX"

            elif List[0] == "3":
                Numeral = "XXX"

            elif List[0] == "4":
                Numeral = "XL"

            elif List[0] == "5":
                Numeral = "L"

            elif List[0] == "9":
                Numeral = "XC"

            if List[1] == "1":
                Numeral = Numeral + "I"

            elif List[1] == "2":
                Numeral = Numeral + "II"

            elif List[1] == "3":
                Numeral = Numeral + "III"

            elif List[1] == "4":
                Numeral = Numeral + "IV"

            elif List[1] == "5":
                Numeral = Numeral + "V"

            print(Numeral)

        elif Arabic_length == 1:

            if List[0] == "1":
                Numeral = "I"

            elif List[0] == "2":
                Numeral = "II"

            elif List[0] == "3":
                Numeral = "III"

            elif List[0] == "4":
                Numeral = "IV"

            elif List[0] == "5":
                Numeral = "V"

            print(Numeral)

        else:
            print("The number must have a minimum of 1 and a maximum of 4 valid digits")


if to_roman_numerals == "No":
    Roman = input(
        "Please enter the Roman Numeral that you want to convert to an Arabic number with a max of MMM, eg. M,M,C,D,I:\n"
    )
    print("The Roman Numeral", Roman, "will be converted to an Arabic Number")
    Roman_Length = len(Roman)
    List = Roman.split(",")
    print(List)
    print("This is the length", Roman_Length)  # length includes spaces

    def roman_to_Arabic():
        Number = 0
        Thousand = 0
        Hundreds = 0
        Tens = 0
        Units = 0
        count = 0
        Z = 0

        if "MMM" in List[:2]:
            Thousand = 3
            List.remove("MMM")

            count = 0
            Z = 0

        elif "MM" in List[:1]:
            Thousand = 2
            List.remove("MM")

            count = 0
            Z = 0

        elif "M" in List[0]:
            Thousand = 1
            List.remove("M")

            count = 0
            Z = 0

        if "CM" in List:
            Hundreds = 9
            List.remove("CM")

            count = 0
            Z = 0

        elif "CD" in List:
            Hundreds = 4
            List.remove("CD")

            count = 0
            Z = 0

        elif "D" in List:
            Hundreds = 5
            List.remove("D")

            count = 0
            Z = 0

        if "CCC" in List:
            Hundreds = 3
            List.remove("CCC")

            count = 0
            Z = 0

        elif "CC" in List:

            Hundreds = 2
            List.remove("CC")

            count = 0
            Z = 0

        elif "C" in List:
            Hundreds = 1
            list.remove("C")

        if "XC" in List:
            Tens = 9
            List.remove("XC")

            count = 0
            Z = 0

        elif "XL" in List:
            Tens = 4
            List.remove("XL")

            count = 0
            Z = 0

        elif "L" in List:
            Tens = 5
            List.remove("L")

            count = 0
            Z = 0

        if "XXX" in List:
            Tens = 3
            List.remove("XXX")

            count = 0
            Z = 0

        elif "XX" in List:
            Tens = 2
            List.remove("XX")

            count = 0
            Z = 0

        elif "X" in List:
            Tens = 1
            List.remove("X")

            count = 0
            Z = 0

        if "IX" in List:
            Units = 9
            List.remove("IX")

            count = 0
            Z = 0

        elif "IV" in List:
            Units = 4
            List.remove("IV")

            count = 0
            Z = 0

        elif "V" in List:
            Units = 5
            List.remove("V")

            count = 0
            Z = 0

        if "III" in List:
            Units = 3
            List.remove("III")

            count = 0
            Z = 0

        elif "II" in List:
            Units = 2
            List.remove("II")

            count = 0
            Z = 0

        elif "I" in List:
            Units = 1
            List.remove("I")

        print("the number is: ", Thousand, Hundreds, Tens, Units)

    roman_to_Arabic()

else:
    print("Type yes or no")
