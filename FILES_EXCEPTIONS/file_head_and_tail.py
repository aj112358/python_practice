# Exercise 149 & 150: Display the Head & Tail of a File

import sys

NUM_LINES = 10


def open_file():

    if len(sys.argv) < 2:
        print("Command line argument for file name omitted.")
        quit()

    file_opened = False
    while not file_opened:
        try:
            file_obj = open(sys.argv[1], "r")
            file_opened = True
        except FileNotFoundError:
            print("File does not exist! Try again...")

    return file_obj


def head(file_obj) -> list:

    line = file_obj.readline().rstrip()
    first_ten = []
    count = 0
    while count < NUM_LINES and line != "":
        first_ten.append(line)
        count += 1
        line = file_obj.readline().rstrip()

    return first_ten


def tail(file_obj) -> list:

    last_ten = []

    line = file_obj.readline().rstrip()
    while line != "":
        if len(last_ten) == NUM_LINES:
            last_ten.pop(0)
        last_ten.append(line)
        line = file_obj.readline().rstrip()

    return last_ten


file = open_file()
head_of_file = head(file)
tail_of_file = tail(file)

print(*head_of_file, sep="\n")
print(*"...", sep="\n")
print(*tail_of_file, sep="\n")

file.close()
