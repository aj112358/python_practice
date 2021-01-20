# This programs evaluates a basic mathematical expression, given via tokens in postfix form.
# Created By: AJ Singh
# Date: Jan 7, 2021

from tokenizing_strings import tokenize, identify_unary
from infix_to_postfix import to_postfix

OPERATORS = list("+-*/^")


# Evaluates a postfix expression, given the tokens.
# @param tokens: List of tokens representing math expression.
# @return: Answer to original math expression.
def evaluate_postfix(postfix: list) -> float:
    """Evaluates tokens in a postfix mathematical expression."""

    values = []

    for token in postfix:

        if token.isdigit():
            values.append(int(token))

        elif token == "u-":
            item = values.pop()
            values.append(-int(item))

        elif token in OPERATORS:
            right = values.pop()
            left = values.pop()

            if token == "^":
                token = "**"

            math = str(left) + token + str(right)
            value = eval(math)

            values.append(value)

    return values[0]


def main():
    math_exp = input("Enter a basic mathematical expression you wish to evaluate:\n")

    tokens = tokenize(math_exp)
    tokens = identify_unary(tokens)
    # print("\nThe tokens are:")
    # print(tokens)

    tokens_postfix = to_postfix(tokens)
    # print("\nThe tokens in postfix form are:")
    # print(tokens_postfix)

    answer = evaluate_postfix(tokens_postfix)
    print("\nThe answer is:", answer)


if __name__ == '__main__':
    main()
