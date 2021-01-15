# Exercise 159: Two Word Random Password

from random import randint


def open_file():

    try:
        word_file = open("words.txt", mode="r")
        return word_file
    except FileNotFoundError:
        print("No such file exists in this directory.")


def create_password(words) -> str:

    num_words = len(words)

    first_word = words[randint(0,num_words-1)].capitalize()
    second_word = words[randint(0,num_words-1)].capitalize()

    while len(first_word) < 3 or len(first_word) > 7:
        first_word = words[randint(0, num_words - 1)].capitalize()

    len_first = len(first_word)

    while len(second_word) != 10-len_first:
        second_word = words[randint(0, num_words - 1)].capitalize()

    return first_word + second_word


def main():
    file_obj = open_file()
    lines = file_obj.readlines()
    words = [word.strip() for word in lines]
    password = create_password(words)
    print("Your random password is:", password)


main()
