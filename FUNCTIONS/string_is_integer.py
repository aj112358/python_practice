# This program determines if a string is an integer, and takes the sign into account.
# Created By: AJ Singh
# Date: Jan 7, 2021


# Check if a string represents a valid integer
# @param num: String to check.
# @return: Boolean value.
def is_integer(num: str) -> bool:
    """Determine if a string represents a valid positive or negative integer."""

    num = num.strip()

    if len(num) == 0:
        return False
    if num.isdigit():
        return True
    if num[0] in ('+', '-'):
        return num[1:].isdigit()

    return False


def main():
    n = input("Enter a string to check if it's a valid integer: ")
    print(is_integer(n))


if __name__ == '__main__':
    main()
