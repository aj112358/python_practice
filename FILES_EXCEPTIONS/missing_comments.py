# Exercise 170: Missing Comments


import sys


def get_lines(file):

    lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def check_comments(lines):
    for num, line in enumerate(lines):
        if line[:4] == "def ":

            try:
                if lines[num - 1][0] != "#":
                    print(f"    Line number {num}: {line[4:-1]}")
            except IndexError:
                print(f"    Line number {num}: {line[4:-1]}")


def main():

    print("\nAll scripts will be checked for missing comments. Any functions with missing comments will be listed.")

    for script in sys.argv[1:]:
        try:
            file_obj = open(script, mode="r")
            print("\nCurrently analyzing: ", script)
            lines = get_lines(file_obj)
            check_comments(lines)

        except FileNotFoundError:
            print("\nUnable to open", script, ". Continuing to next script...")


main()
