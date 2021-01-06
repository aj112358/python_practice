#### This program determines if an integer is a perfect number.
# It can also be used to list all perfect numbers less than given amount.
# Created By: AJ Singh
# Date: Jan 6, 2021

from proper_divisors import divisors


# Determines whether an integer is perfect
# @param n: Integer to check.
# @return: Boolean indicating if perfect
def is_perfect(n: int) -> bool:
    """Determine if a number is a perfect number."""
    factors = divisors(n)

    total = 0
    for factor in factors[:-1]:
        total += factor

    return total == n


def main():
    for num in range(1,10001):
        if is_perfect(num):
            print(num)
    # n = int(input("Please enter the integer you wish to check: "))
    # print(is_perfect(n))


if __name__ == '__main__':
    main()
