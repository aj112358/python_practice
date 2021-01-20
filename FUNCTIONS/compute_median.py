####
# This program computes and displays the median of three values.
# Created by: AJ Singh
# Date: January 5, 2020

# Compute the median of three values.
# @param a: The first value.
# @param b: The second value.
# @param c: The third value.
# @return: The median of a,b,c.
def median(a, b, c):
    """Computes the median of three values."""

    return a + b + c - min(a, b, c) - max(a, b, c)


def main():
    x = float(input("Please enter the first value: "))
    y = float(input("Please enter the second value: "))
    z = float(input("Please enter the third value: "))

    m = median(x, y, z)
    print("The median of the three numbers is: ", m)


if __name__ == "__main__":
    main()
