# This program simulates two dice rolls.
# Created By: AJ Singh
# Date: Jan 8, 2021

from random import randint
from tabulate import tabulate

# Expected values for two dice rolls
EXPECTATIONS = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Headers for output table
HEADERS = ["Total", "Rolls", "Sim. %", "Exp. %"]


# Rolls two fair 6-sided die and computes sum of rolls.
# @params: None
# @return: Sum of two rolls.
def dice_roll():
    """Rolls two 6-sided dice and computes total."""

    first_roll = randint(1, 6)
    second_roll = randint(1, 6)

    return first_roll + second_roll


def main():
    results = {k:[0,0] for k in range(2, 13)}

    num_rolls = 5000000
    for _ in range(num_rolls):
        roll_sum = dice_roll()
        results[roll_sum][0] += 1

    # Computes simulated percentage for each sum rolled
    for key in results:
        results[key][1] = round(results[key][0]/num_rolls * 100, 2)

    # Creates table for output
    table = []
    for (k, v), e in zip(results.items(), EXPECTATIONS):
        data = [k, v[0], v[1], round(e*100, 2)]
        table.append(data)
    print(tabulate(table, HEADERS))


if __name__ == '__main__':
    main()
