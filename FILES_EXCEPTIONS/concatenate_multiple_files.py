# Exercise 151: Concatenate Multiple Files

import sys

if len(sys.argv) < 2:
    print("No command line arguments given!")
    quit()

for file_name in sys.argv[1:]:

    try:
        file = open(file_name)
    except FileNotFoundError:
        print("\nUnable to open file", file_name, "\n")

    content = file.read()
    print(content)
    print()

