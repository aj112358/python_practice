# This program converts a list of tokens representing a mathematical expression, and
# converts it from infix form to postfix form.
# Created By: AJ Singh
# Date: Jan 7, 2021

from tokenizing_strings import tokenize, identify_unary
from string_is_integer import is_integer
from operator_precedence import precedence

OPERATORS = list("+-*/^") + ['u+', 'u-']


# Converts tokens of a math expression from infix form to postfix form.
# @param infix: List of tokens for a math expression.
# @return: List of tokens in postfix form.
def to_postfix(infix: list) -> list:
    """Convert a list of mathematical tokens to postfix form."""

    operators = []
    postfix = []

    for token in infix:
        if is_integer(token):
            postfix.append(token)

        if token in OPERATORS:
            while len(operators) > 0 and \
                    operators[-1] != "(" and \
                    precedence(token) < precedence(operators[-1]):
                item = operators.pop()
                postfix.append(item)

            operators.append(token)

        if token == "(":
            operators.append(token)

        if token == ")":
            while operators[-1] != "(":
                item = operators.pop()
                postfix.append(item)
            operators.pop()

    while len(operators) > 0:
        item = operators.pop()
        postfix.append(item)

    return postfix


def main():
    math_exp = input("Enter a basic mathematical expression:\n")

    tokens = tokenize(math_exp)
    tokens = identify_unary(tokens)
    print("\nThe tokens are:")
    print(tokens)

    tokens_postfix = to_postfix(tokens)
    print("\nThe tokens in postfix form are:")
    print(tokens_postfix)


if __name__ == '__main__':
    main()
