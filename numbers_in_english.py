# This program writes the English equivalent of a number (0-999).
# Created By: AJ Singh
# Date: Jun 8, 2021

# NOTE: This code works, but could do with some editing/refactoring.


DIGITS = {'0': "zero",
          '1': "one",
          '2': "two",
          '3': "three",
          '4': "four",
          '5': "five",
          '6': "six",
          '7': "seven",
          '8': "eight",
          '9': "nine"}

DOUBLES = {'10': "ten",
           '11': "eleven",
           '12': "twelve",
           '13': "thirteen",
           '14': "fourteen",
           '15': "fifteen",
           '16': "sixteen",
           '17': "seventeen",
           '18': "eighteen",
           '19': "nineteen"}

TENS = {'00': "",
        '10': "ten",
        '20': "twenty",
        '30': "thirty",
        '40': "forty",
        '50': "fifty",
        '60': "sixty",
        '70': "seventy",
        '80': "eighty",
        '90': "ninety"}

HUNDREDS = {'100': "one hundred",
            '200': "two hundred",
            '300': "three hundred",
            '400': "four hundred",
            '500': "five hundred",
            '600': "six hundred",
            '700': "seven hundred",
            '800': "eight hundred",
            '900': "nine hundred"}


def to_english(num: str) -> str:
    """Convert a number to its equivalent English translation."""

    answer = ""
    size = len(num)

    if size >= 1:

        if num in DIGITS:
            return DIGITS[num]

        else:  # size >= 2:

            if num[-2:] in DOUBLES:
                answer = DOUBLES[num[-2:]]
            elif num[-2:] in TENS:
                answer = TENS[num[-2:]]
            else:
                answer = TENS[num[-2]+'0'] + " " + DIGITS[num[-1]]

            if size == 3:

                if num in HUNDREDS:
                    return HUNDREDS[num]
                else:
                    answer = DIGITS[num[-3]] + " hundred " + answer

    return answer



# tests = ['0', '1', '9', '10', '11', '19', '20', '21', '89', '90', '91', '99', '100', '101', '110', '111', '119', '120', '121']
# for test in tests:
#     print(to_english(test))

for _ in range(1000):
    print(_, to_english(str(_)))

# DONT WORK: 100

# while True:
#     n = input("\nEnter a number: ")
#     print(to_english(n))