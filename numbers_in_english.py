# This program writes the English equivalent of a number (0-999).
# Created By: AJ Singh
# Date: Jun 8, 2021


DIGITS = {1: "one",
           2: "two",
           3: "three",
           4: "four",
           5: "five",
           6: "six",
           7: "seven",
           8: "eight",
           9: "nine"}

NUMBERS = {1: "eleven",
           2: "twelve",
           3: "thirteen",
           4: "fourteen",
           5: "fifteen",
           6: "sixteen",
           7: "seventeen",
           8: "eighteen",
           9: "nineteen"}

TENS = {1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"}




def to_english(num: int) -> str:
    """Convert a number to its equivalent English translation."""

    string = str(num)
    if len(str(num)) == 1:
        if num == 0:
            return "zero"
        return DIGITS[num]

    if len(str(num)) == 2:
        if string[-1] == '0':
            return TENS[int(string[0])]
        elif string[0] == '1':
            return NUMBERS[int(string[1])]
        else:
            return TENS[int(string[0])] + " " + DIGITS[int(string[1])]

    if len(str(num)) == 3:



# number = 20
# print(to_english(number))

for _ in range(100):
    print(to_english(_))