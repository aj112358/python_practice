# This program creates a bingo card.
# Created By: AJ Singh
# Date: Jan 8, 2021

from random import randint
from pprint import pprint
from tabulate import tabulate

COLUMN_NAMES = list("BINGO")


def bingo_card():
    """Create a bingo card. Duh!"""

    card = {column:[] for column in COLUMN_NAMES}

    multiple = 0
    for k in card:
        for _ in range(5):
            card[k].append(randint(multiple+1, multiple+15))
        multiple += 15

    return card


def main():
    card = bingo_card()
    print(tabulate(card, COLUMN_NAMES))


if __name__ == '__main__':
    main()



