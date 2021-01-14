# Exercise 155: Words that Occur Most


# C:\Users\AJ\PycharmProjects\python_practice\only_the_words.py
from ..only_the_words import extract_words
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
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    return frequency


def main():
    file_obj = open_file()
    sentences = file_obj.readlines()
    freq = word_frequency(sentences)
    print(freq)


main()
