# This program makes and shuffles a standard deck of cards.
# Created By: AJ Singh
# Date: Jan 7, 2021

from random import randint

SUITS = ['d', 'c', 'h', 's']
DENOMINATIONS = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']


# Creates a standard deck of cards
# @params: None
# @return: Complete deck of cards.
def create_deck() -> list:
    """Creates a standard 52-card deck."""

    deck = []
    for suit in SUITS:
        for denom in DENOMINATIONS:
            card = str(denom)+suit
            deck.append(card)

    return deck


# Shuffles a deck of cards
# @param deck: Deck of cards to be shuffled.
# return: Shuffled deck.
def shuffle(deck: list) -> list:
    """Shuffle a deck of cards."""

    shuffled = deck.copy()

    for i in range(len(shuffled)-1):
        new_index = randint(i, len(shuffled)-1)

        shuffled[i], shuffled[new_index] = \
            shuffled[new_index], shuffled[i]

    return shuffled


def main():
    deck = create_deck()
    print(deck)
    print("Shuffling.....")
    shuffled_deck = shuffle(deck)
    print(shuffled_deck)


if __name__ == '__main__':
    main()
