# This program checks if a bingo card is a winner.
# Created By: AJ Singh
# Date: Jan 8, 2021

from tabulate import tabulate

KEYS = list("BINGO")


# Check a bingo card for a winner.
# @param card: Bingo card to check.
# @return: Boolean value indicating a winner.
def is_winner(card: dict) -> bool:
    """Check if a bingo card is a winner."""

    # Check for vertical zeros
    for column in card:
        if sum(card[column]) == 0:
            # print(f"Winner (on column {column})!!!")
            return True

    # Check for horizontal zeros
    for _ in range(5):
        total = 0
        for row in card.values():
            total += row[_]
        if total == 0:
            # print(f"Winner (on row {_+1})!!!")
            return True

    # Check diagonals
    down, up = 0, 0
    for key in card:
        if card[key][down] == 0:
            down += 1
        if card[key][-1-up] == 0:
            up += 1
    if down == 5:
        # print("Winner (on down diagonal)!!!")
        return True
    if up == 5:
        # print("Winner (on up diagonal)!!!")
        return True

    # print("You lost... =(")
    return False


def main():

    card = {"B": [0, 4, 0, 0, 0],
            "I": [0, 6, 1, 0, 0],
            "N": [1, 0, 9, 8, 5],
            "G": [0, 0, 0, 0, 4],
            "O": [0, 0, 2, 0, 0]}

    print(tabulate(card, KEYS))
    print()
    print(is_winner(card))


if __name__ == "__main__":
    main()
