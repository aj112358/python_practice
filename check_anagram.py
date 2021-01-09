# This program determines if two words/sentences are anagrams.
# Created By: AJ Singh
# Date: Jan 8, 2021

from string import punctuation, whitespace

EXTRANEOUS = punctuation + whitespace


# Determine whether two strings are anagrams of one another.
# @params string1, string2: The two strings to compare.
# @return: Boolean value representing if they're anagrams.
def are_anagrams(string1: str, string2: str) -> bool:
    """Determine if two string are anagrams. Ignores capitalization, punctuation, and spacing."""

    string1 = string1.lower()
    string2 = string2.lower()

    characters1 = {}
    characters2 = {}

    for char in string1:
        if char in EXTRANEOUS:
            continue
        if char in characters1:
            characters1[char] += 1
        else:
            characters1[char] = 1

    for char in string2:
        if char in EXTRANEOUS:
            continue
        if char in characters2:
            characters2[char] += 1
        else:
            characters2[char] = 1

    return characters1 == characters2


def main():

    first = input("Enter first word/sentence: ")
    second = input("Enter second word/sentence: ")

    print(are_anagrams(first, second))


if __name__ == '__main__':
    main()


