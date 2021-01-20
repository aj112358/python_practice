# Exercise 85: Compute the Hypotenuse

from math import sqrt


def hypotenuse(a, b):
    """Function to compute the hypotenuse of a right triangle."""

    c = sqrt(a**2 + b**2)

    return c


def main():

    a = float(input("What is the length of one leg: "))
    b = float(input("What is the length of other leg: "))

    c = hypotenuse(a, b)
    print("The hypotenuse length is: ", c)


if __name__ == "__main__":
    main()


# Exercise 86: Taxi Fare

BASE_FARE = 4.00
VARIABLE_FARE = 0.25  # per 140 meters travelled
VARIABLE_DIST = 140

def taxi_fare(total_distance):
    """Compute amount owing for taxi ride given distance travelled."""

    fare = BASE_FARE + VARIABLE_FARE*total_distance/VARIABLE_DIST
    return fare

def main():

    distance = float(input("What distance did you travel? "))
    fare = taxi_fare(distance)

    print("You owe: ", round(fare, 2))

if __name__ == "__main__":
    main()


# Exercise 87: Shipping Calculator
# Trivial

# Exercise 89: Integer to Ordinal Number
# Trivial

# Exercise 90: The Twelve Days of Christmas
# Trivial (Can probably use the solution to previous exercise!)

# Exercise 91: Gregorian Date to Ordinal Date
# Trivial (Can use my code for determining leap year)

# Exercise 92: Ordinal Date to Gregorian Date
# Trivial (be careful about leap years!)

# Exercise 93: Center a String in the Terminal Window
# Trivial

# Exercise 95: Capitalize It
# Trivial

# Exercise 98: Is a Number Prime?
# Skip (look at number theory primality tests)

# Exercise 99: Next Prime
# Skip (look at number theory primality tests)
# Can use function created in previous exercise.

# Exercise 100: Random Password
# Trivial

# Exercise 101: Random License Plate
# Trivial

# Exercise 103: Random Good Password
# Trivial

# Exercise 104: Hexadecimal and Decimal Digit
# Do later

# Exercise 105: Arbitrary Base Conversions
# Do later

# Exercise 106: Days in a Month
# Trivial

# Exercise 107: Reduce a Fraction
# Trivial

# Exercise 108: Reduce Measures
# Trivial (same problem as 'making change')

# Exercise 109: Magic Dates
# Trivial


