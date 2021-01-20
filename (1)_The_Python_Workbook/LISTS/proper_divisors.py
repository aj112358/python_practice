### This program compute the list of proper divisors of an integer
# Created By: AJ Singh
# Date: Jan 6, 2021

from math import sqrt, floor


# This function computes the divisors of an integer
# @param n: Input to factor.
# @return: List of divisors.
def divisors(n: int) -> list:
    """Compute all the (positive) divisors of an integer."""
    factors = []
    for i in range(1, floor(sqrt(n))+1):

        if n % i == 0:
            factors.append(i)
            if i**2 != n:
                factors.append(int(n/i))

    factors.sort()
    return factors


def main():

    n = int(input("What integer do you want to factor? "))
    factors = divisors(n)
    print("The factors are: ", factors)


if __name__ == '__main__':
    main()
