# This program is an implementation of the Sieve of Eratosthenes
# Created By: AJ Singh
# Date: Jan 7, 2021


# Computes primes
# @param n: Upper limit to compute up to.
# @return: List of prime numbers up to n.
def compute_primes(n: int) -> list:
    """Prime number generator using Sieve of Eratosthenes."""

    numbers = [i for i in range(n+1)]
    primes = []

    p = 2
    while p < n:
        for index in range(2 * p, n + 1, p):
            numbers[index] = 0
        p += 1

    for num in numbers:
        if num not in (0, 1):
            primes.append(num)

    return primes


def main():
    n = int(input("Enter an upper bound: "))
    print(f"The primes numbers up to {n} are:")
    print(compute_primes(n))


if __name__ == "__main__":
    main()
