# Exercise 167: Spell Checker
# Misspelled words are identified by checking against a given list of words.
# Any word that doesn't appear in this file is considered to be misspelled.
# Hence, a word *may* be mistakenly categorized as misspelled.
# Does not take into account contractions.


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


def get_dictionary():

    with open("words.txt", mode="r") as dictionary:

        lines = dictionary.readlines()
        words = set(map(lambda x: x.strip().lower(), lines))
    return words


def check_spelling(to_check: str):
    for word in to_check:
        if word in get_dictionary():
            continue
        else:
            print("A typo found: ", word)


def main():
    file_obj = open_file()
    data = file_obj.read()
    words_to_check = set(map(lambda x: x.lower(), extract_words(data)))
    get_dictionary()
    check_spelling(words_to_check)


main()
