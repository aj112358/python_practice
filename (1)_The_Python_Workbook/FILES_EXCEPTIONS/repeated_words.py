# Exercise 168: Repeated Words
# This program looks for accidental duplicate words in a document.

import sys
from only_the_words import extract_words

if len(sys.argv) < 2:
    print("Please include the file to spell-check in a command line argument.")
    quit()


def open_file():
    try:
        file_to_check = open(sys.argv[1], mode="r")
        return file_to_check
    except FileNotFoundError:
        print("File not found. Please try again.")


def check_for_repeats(data):
    prev_word = ""
    for index3, line in enumerate(data):
        index = 0
        for index2, word in enumerate(line):

            if line[0] == prev_word:
                print(f"Double word in line {index3 + 1} (with end of previous line): {prev_word}")
                prev_word = ""

            try:
                if line[index] == line[index + 1]:
                    print(f"Double word in line {index3 + 1}: {word}")
            except IndexError:
                prev_word = line[index]
            index += 1


def main():
    file_obj = open_file()
    lines = file_obj.readlines()

    data = list(map(lambda x: extract_words(x.lower()), lines))
    print("\n")

    check_for_repeats(data)

    file_obj.close()


main()
