# Exercise 154: Letter Frequency Analysis.

from string import ascii_uppercase
from string import punctuation
from string import digits
import sys

if len(sys.argv[1]) < 2:
    print("Input file needed.")
    quit()


def open_file():

    try:
        file = open(sys.argv[1], mode="r")
        return file
    except FileNotFoundError:
        print("Unable to open file.")


# Determine frequency of letters.
def letter_frequency(words):

    freq = {}
    for word in words:
        for char in word:

            if char in list(punctuation) or char in list(digits):
                continue

            if char.upper() in freq:
                freq[char.upper()] += 1
            else:
                freq[char.upper()] = 1

    return freq


def main():
    file_obj = open_file()
    words = file_obj.read().split()
    file_obj.close()
    freq = letter_frequency(words)

    for k, v in freq.items():
        print(f"{k}:{v}")


main()
