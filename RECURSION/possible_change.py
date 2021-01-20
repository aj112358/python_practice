# Exercise 181: Possible Change
# Determines whether or not it is possible to make
# a particular total using a specific number of coins.
# ASSUMPTION: We have: quarters, dimes, nickels, pennies


# 0.25q + 0.1d + 0.05n + 0.01p = dollar
# q+d+n+p = coins
# 9 d + 4 n + 24 q = 100*dollar - coins

from math import floor

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

COINS = "QUARTER,DIME,NICKEL,PENNY".split(",")
change = {'QUARTER': 0, 'DIME': 0, 'NICKEL': 0, 'PENNY': 0}


def is_possible_change(dollar: float, coins: int):

    if coins == 0:
        return True
    if coins < 0:
        return False

    num_quarters = floor(dollar // QUARTER)
    remaining = round(dollar % QUARTER, 2)
    if num_quarters == coins:
        return True
    else:
        return is_possible_change(remaining, coins - num_quarters)

    num_dimes = floor(remaining // DIME)
    remaining = round(dollar % DIME, 2)
    if remaining != 0:
        return is_possible_change(remaining, coins - num_dimes)

    num_nickels = floor(remaining // NICKEL)
    remaining = round(dollar % NICKEL, 2)
    if remaining != 0:
        return is_possible_change(remaining, coins - num_nickels)

    num_pennies = floor(remaining // PENNY)
    remaining = round(dollar % PENNY, 2)
    if remaining != 0:
        return is_possible_change(remaining, coins - num_pennies)

    print("Hello")
    # return False


def main():
    dollar_amount = round(float(input("Dollar amount: ")), 2)
    num_coins = int(input("Number of coins: "))

    result = is_possible_change(dollar_amount, num_coins)
    print(result)


main()
