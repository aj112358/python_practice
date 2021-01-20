# Exercise 152: Number the Lines in a File

import sys

if len(sys.argv) < 3:
    print("Not enough command line arguments given.")
    quit()


try:
    read_file = open(sys.argv[1], mode="r")
    write_file = open(sys.argv[2], mode="w")
except FileNotFoundError:
    print("Error opening the read-in file", read_file)
    quit()

line = read_file.readline()
num = 1
while line != "":
    new_line = str(num) + ": " + line
    write_file.write(new_line)
    num += 1
    line = read_file.readline()

read_file.close()
write_file.close()
