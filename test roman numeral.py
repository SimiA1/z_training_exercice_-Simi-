to_roman_numerals = input(
    "if you would like to convert TO a roman numeral type Yes, if not type No:\n"
)


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

        if "C" in List:
            Hundreds = 1
            list.remove("C")

        print("the number is: ", Thousand, Hundreds, Tens, Units)
        print(List)

    roman_to_Arabic()

else:
    print("Type yes or no")
