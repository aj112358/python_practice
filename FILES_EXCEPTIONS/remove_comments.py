# Exercise 158: Remove Comments from Python File.

import sys

if len(sys.argv) < 2:
    print("Not enough command line arguments.")
    quit()


def open_files():

    try:
        in_file = open(sys.argv[1], mode="r")
        return in_file
    except FileNotFoundError:
        print("Unable to open file.")


def remove_comments(lines):

    fixed_lines = []
    for line in lines:
        x = line.find("#")
        if x != -1:
            line = line[:x]
        fixed_lines.append(line)

    return fixed_lines


def create_new_file(lines):

    out_file = open(sys.argv[2], mode="w")
    out_file.writelines(lines)
    out_file.close()


def main():
    file_obj = open_files()
    lines = file_obj.readlines()
    fixed_lines = remove_comments(lines)
    create_new_file(fixed_lines)
    file_obj.close()


main()
