# This program simulates a bingo game for a single card.
# Created By: AJ Singh
# Date: Jan 8, 2021

from bingo_card import bingo_card
from check_bingo_card import is_winner
from random import shuffle
from tabulate import tabulate
import time

COLUMN_NAMES = list("BINGO")


# Decorator for runtime of a function.
def timing(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        delta = end - start  # In milliseconds.

        x = delta / 1000
        seconds = x % 60
        x /= 60
        minutes = x % 60
        x /= 60
        hours = x % 24

        print("Simulation time: {}-{}-{}".format(hours, minutes, seconds))

        return result
    return timed


# Generates list of 75 bingo balls.
# @params: None
# @return: List of bingo balls.
def generate_balls() -> list:
    """Generates list of 75 bingo balls, from B1 to O75."""

    bingo_balls = []
    multiple = 0
    for letter in COLUMN_NAMES:
        for i in range(1+multiple, 16+multiple):
            bingo_balls.append(letter+str(i))
        multiple += 15

    shuffle(bingo_balls)
    return bingo_balls


# Simulates one entire game of bingo with one card.
# @params: None
# @return: Number of calls needed to win.
def play_bingo() -> int:
    """Simulate one game of bingo. Returns the number of calls needed to win."""

    # print("\nWelcome to BINGO!!!. Here is your card:")
    card = bingo_card()
    # print(tabulate(card, COLUMN_NAMES))

    balls = generate_balls()
    # print("\nPlaying bingo.......")

    while not is_winner(card):
        call = balls.pop()
        # print(call)
        letter, number = call[0], int(call[1:])

        if number in card[letter]:
            i = card[letter].index(number)
            card[letter][i] = 0

    # print()
    # print(tabulate(card, COLUMN_NAMES))
    # print("="*50)

    num_calls = 75-len(balls)
    return num_calls


@timing
def main():

    call_results = {}
    simulations = int(input("How many simulations of a bingo game? "))

    for _ in range(simulations):
        result = play_bingo()

        if result in call_results:
            call_results[result] += 1
        else:
            call_results[result] = 1

    print("\nMinimum number of calls:", min(call_results.keys()))
    print("Maximum number of calls:", max(call_results.keys()))

    # Code block for computing average number of calls.
    total = 0
    for key, value in call_results.items():
        total += key*value
    avg = total/simulations

    print("Average number of calls:", round(avg, 2))
    print("Percent of balls used: {}%".format(round(avg/75*100, 2)))


if __name__ == "__main__":
    main()
