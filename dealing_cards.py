# This programs deals cards from a deck.
# Created By: AJ Singh
# Date: Jan 7, 2021

from shuffle_deck_of_cards import create_deck, shuffle


# Splits deck of cards into hands, each with same number of cards
# @param num_hands: The number of players in the game.
# @param cards_per_hand: How many cards for each player
# @param deck: Deck to use for the game.
# @return: List of hands (each hand is itself a list)
def deal(num_hands: int, cards_per_hand: int, deck: list) -> list:
    """Deals cards."""

    # Check if there are enough cards for each hand
    if num_hands * cards_per_hand > len(deck):
        print("\nNot enough cards to go around!")
        return []

    dealt_hands = []  # Will contain list of hands

    # Instantiate the lists representing each hand
    for _ in range(num_hands):
        dealt_hands.append([])

    # Dealing the hands
    for _ in range(cards_per_hand):
        for hand in dealt_hands:
            hand.append(deck.pop())

    return dealt_hands


def main():
    deck = create_deck()
    shuffled = shuffle(deck)
    print("Here is your shuffled deck:")
    print(shuffled)

    num_players = int(input("\nHow many players? "))
    num_cards = int(input("How many cards per player? "))

    hands = deal(num_players, num_cards, shuffled)
    print("\nHere are the hands dealt:")
    for i, hand in enumerate(hands):
        print(f"Hand {i+1}:", hand)

    print("\nCards remaining in deck:")
    print(shuffled)


if __name__ == '__main__':
    main()
