# Exercise 181: Possible Change
# Determines whether or not it is possible to make
# a particular total using a specific number of coins.
# ASSUMPTION: We have: quarters, dimes, nickels, pennies

from math import floor

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

COINS = ['QUARTER', 'DIME', 'NICKEL', 'PENNY']


def is_possible_change(dollar: float, coins: int):

    change = {'QUARTER': 0, 'DIME': 0, 'NICKEL': 0, 'PENNY': 0}

    if dollar == 0.00:
        if sum(change.values()) == coins:
            return True
        else:
            return False

            num_quarters = floor(dollar // QUARTER)
            change['QUARTER'] = num_quarters
            dollar = dollar % QUARTER

            num_dimes = floor(dollar // DIME)
            change['DIME'] = num_dimes
            dollar = dollar % DIME

            num_nickels = floor(dollar // NICKEL)
            change['NICKEL'] = num_nickels
            dollar = dollar % NICKEL

            num_pennies = floor(dollar // PENNY)
            change['PENNY'] = num_pennies
            dollar = dollar % PENNY


    return is_possible_change(round(dollar, 2), coins - num_quarters)









def main():
    dollar_amount = round(float(input("Dollar amount: ")), 2)
    num_coins = int(input("Number of coins: "))

    result = is_possible_change(dollar_amount, num_coins)
    print(result)


main()
