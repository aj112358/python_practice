# Exercise 177: Roman Numerals

# Only C, X and I are used in a subtractive manner.
# The numeral that a C, X or I precedes must have a value that is
# no more than 10 times the value being subtracted.
#
# As such, I can precede V or X, but it cannot precede L, C, D or M.
# This means, for example, that 99 must be represented by XCIX
# rather than by IC.
#
# So, if we have AB, then either:
#   (i)  A >= B
#   (ii) If A < B, then B <= 10*A (and return B-A)

ROMAN = {'M': 1000,
         'D': 500,
         'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1}


# This function does NOT do any error checking!!!!
def roman_to_integer(x: str) -> int:

    x = x.upper()

    if len(x) == 0:
        return 0
    if len(x) == 1:
        return ROMAN[x]

    A, B = x[0], x[1]
    if ROMAN[A] >= ROMAN[B]:
        return ROMAN[A] + ROMAN[B] + roman_to_integer(x[2:])
    else:
        return ROMAN[B] - ROMAN[A] + roman_to_integer(x[2:])


def main():
    roman_numeral = input("What Roman numeral to convert: ").upper()
    integer = roman_to_integer(roman_numeral)
    print(f"\nThe Roman numeral {roman_numeral} is {integer}.")


main()
