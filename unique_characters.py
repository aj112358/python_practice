# This program determines the number of unique characters in a string.
# Created By: AJ Singh
# Date: Jan 8, 2021

from pprint import pprint


# Places characters of string into a dictionary to count them.
# @param string: String to count characters for.
# @return: Dictionary of character counts.
def check_unique(string: str) -> dict:
    """Determine unique characters."""

    characters = {}

    for char in string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters


def main():
    user_string = input("Enter a string to analyze: ")
    result = check_unique(user_string)

    print("Here are the unique characters in your string, along with their frequency:")

    pprint(result, width=1)


if __name__ == '__main__':
    main()
