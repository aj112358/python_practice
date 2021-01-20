# Exercise 153: Find the Longest Word in a File
# NOTE: A 'word' will include any attached punctuation!

import sys


def open_file():

    try:
        file = open(sys.argv[1])
        return file
    except FileNotFoundError:
        print("Unable to locate file.")


def count_words(words) -> dict:

    word_frequency = {}
    for word in words:
        if len(word) in word_frequency:
            word_frequency[len(word)].append(word)
        else:
            word_frequency[len(word)] = [word]

    return word_frequency


def print_results(word_frequency):
    longest_length = max(word_frequency.keys())
    longest_words = set(word_frequency[longest_length])

    print("The longest word length is:", longest_length)
    print("\nThe longest words are:")
    for word in longest_words:
        print(word, sep="  ")


def main():
    file_obj = open_file()
    word_list = file_obj.read().split()
    freq = count_words(word_list)
    print_results(freq)


main()
