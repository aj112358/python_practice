# This function tokenizes a basic mathematical expression.
# Math expression can include: + - * / ^ ( ) =, and digits
# Assumes all numbers are integers (no decimal numbers).
# Any sequence of consecutive digits is considered one token
#   THUS: Don't include spaces within a number!
# Created By: AJ Singh
# Date: Jan 7, 2021

OPERATORS = list("+-*/^")
DIGITS = [str(i) for i in range(10)]
BRACKETS = "()"


# Creates list of tokens given a basic math expression
# @params math_exp: The math expression to tokenize.
# @return: A list of the tokens.
def tokenize(math_exp: str) -> list:
    """Tokenizes a basic mathematical operation. \
    (Assumes all numbers are integers; Do not include spaces within a number)."""

    tokens = []
    digit_string = ""  # Used for tokenizing a number.

    for term in math_exp:

        if term in OPERATORS or term in BRACKETS:
            if digit_string != "":  # Tokenize number first, before symbol.
                tokens.append(digit_string)
                digit_string = ""
            tokens.append(term)

        elif term in DIGITS:
            digit_string += term

        else:  # To deal with numbers with spaces on either side.
            if digit_string != "":
                tokens.append(digit_string)
                digit_string = ""

    # Runs if last term is only a number, with no ending symbol
    if digit_string != "":
        tokens.append(digit_string)

    return tokens


# Given a list of tokens, determines if any operators are unary
# @param tokens: List of tokens to check.
# @return: Modified list of tokens with unary operators marked.
def identify_unary(tokens: list) -> list:
    """Determine if there are any unary + or - operators, and mark them."""

    tokens_unary = tokens.copy()

    if tokens_unary[0] == '+':
        tokens_unary[0] = 'u+'
    if tokens_unary[0] == '-':
        tokens_unary[0] = 'u-'

    for i in range(1, len(tokens_unary)):
        if tokens_unary[i] == '+':
            if tokens_unary[i - 1] in OPERATORS or tokens_unary[i - 1] == "(":
                tokens_unary[i] = 'u+'

        if tokens_unary[i] == '-':
            if tokens_unary[i - 1] in OPERATORS or tokens_unary[i - 1] == "(":
                tokens_unary[i] = 'u-'

    return tokens_unary


def main():
    math_expr = input("Type in a math expression: \n")
    tokens = tokenize(math_expr)
    tokens = identify_unary(tokens)
    print("Here are the tokens:\n")
    print(tokens)


if __name__ == "__main__":
    main()
