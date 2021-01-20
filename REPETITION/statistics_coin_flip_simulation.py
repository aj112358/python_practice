# Exercise 84: Coin Flip Simulation

from random import choice


def coin_flips():

    SAMPLE_SPACE = ('H', 'T')

    first_toss = choice(SAMPLE_SPACE)
    second_toss = choice(SAMPLE_SPACE)

    # print(first_toss, end=" ")
    # print(second_toss, end=" ")

    flips = 2
    while True:

        coin_toss = choice(SAMPLE_SPACE)
        flips += 1
        # print(coin_toss, end=" ")

        if first_toss == second_toss == coin_toss:
            # print(f"({flips} flips)")
            break
        else:
            first_toss = second_toss
            second_toss = coin_toss

    return flips


total = 0
SIMULATIONS = 1000000
for _ in range(SIMULATIONS):
    total += coin_flips()

print("Average number of flips: ", total/SIMULATIONS)
