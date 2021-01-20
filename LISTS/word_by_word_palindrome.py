#### This program determines if a sentence is a word-by-word palindrome.
# Created By: AJ Singh
# Date: Jan 6, 2021

from math import floor
from only_the_words import extract_words


# Determine whether a sentence is a word-by-word palindrome.
# @param sentence: String to check.
# @return: Boolean value.
def is_palindrome(sentence: str) -> bool:
    """Check if a string is a word-by-word palindrome."""

    words = extract_words(sentence)
    middle = floor(len(words)/2)

    for index in range(middle):
        if words[index].lower() != words[len(words)-index-1].lower():
            return False

    return True


def main():
    sentence = input("Enter a sentence to check (punctuation is okay):")
    print(is_palindrome(sentence))


if __name__ == "__main__":
    main()
