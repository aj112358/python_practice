#  Exercise 172: Words with Six Vowels in Order

import sys

VOWELS = set("aeiouy")

if len(sys.argv) < 2:
    print("Missing file of words to check.")
    quit()


def open_file():
    try:
        file = open(sys.argv[1], mode="r")
        return file
    except FileNotFoundError:
        print("Unable to open file.")
        quit()


def check_for_words(words):

    for word in words:
        if len(word) < 6:
            continue

        vowels = []
        for char in word:
            if char in VOWELS:
                vowels.append(char.lower())

        vowels = "".join(vowels)
        if vowels == "aeiouy":
            print(word)


def main():
    file_obj = open_file()
    words = set(file_obj.read().splitlines())
    # print(words)
    check_for_words(words)


main()
