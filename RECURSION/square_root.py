# Exercise 179: Recursive Square Roots


def square_root(n: float, guess: float = 1.0) -> float:

    if abs(guess**2 - n) < 1e-12:
        return guess

    new_guess = (guess + n/guess)/2

    return square_root(n, new_guess)


def main():
    num = float(input("What number to square root: "))
    print(round(square_root(num), 5))


main()
