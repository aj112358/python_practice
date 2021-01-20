# Exercise 155: Words that Occur Most


# C:\Users\AJ\PycharmProjects\python_practice\only_the_words.py
# from ..only_the_words import extract_words
from only_the_words import extract_words
import sys


def open_file():

    try:
        file = open(sys.argv[1])
        return file
    except FileNotFoundError:
        print("File not found!")


def word_frequency(sentences):

    frequency = {}
    for _ in sentences:
        words = extract_words(_)

        for word in words:
            if word.lower() in frequency:
                frequency[word.lower()] += 1
            else:
                frequency[word.lower()] = 1

    return frequency


def print_results(freq: dict):

    max_freq = max(freq.values())
    most_freq_words = []

    for word in freq:
        if freq[word] == max_freq:
            most_freq_words.append(word)

    print(f"\nThe most frequent word(s) occur {max_freq} times.")
    print("\nThese word(s) are:\n")
    print(*most_freq_words, sep="\n")


def main():
    file_obj = open_file()
    sentences = file_obj.readlines()
    freq = word_frequency(sentences)
    print_results(freq)


main()
