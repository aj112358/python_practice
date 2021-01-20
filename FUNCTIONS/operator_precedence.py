# This program determines the precedence of a basic math operator as follows:
#   1 for +, -
#   2 for *, /
#   3 for unary +, -
#   4 for ^
# Created By: AJ Singh
# Date: Jan 7, 2021


# Determine precedence based on above criteria.
# @param operator: Input operator to check.
# @return: Integer as per above criteria.
def precedence(operator: str) -> int:
    """Returns precedence of mathematical operator."""

    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    elif operator in ('u+', 'u-'):
        return 3
    elif operator == '^':
        return 4
    else:
        return -1


def main():
    math = input("Which operator to check: ")
    result = precedence(math)

    print(result) if result != -1 else print("Error!")


if __name__ == '__main__':
    main()

