####
# This program determines whether a triangle can be constructed given three side lengths..
# Created by: AJ Singh
# Date: January 5, 2020

# Determine whether a triangle is valid
# @param a, b, c: Lengths
# @return: Boolean value for being a valid triangle
def is_valid_triangle(a, b, c):
    '''Given three lengths, determines whether a triangle can be created'''

    if a <= 0 or b <= 0 or c <= 0:
        return False

    semi_perimeter = (a + b + c) / 2
    if a >= semi_perimeter or c >= semi_perimeter or b >= semi_perimeter:
        return False

    return True


def main():
    x = float(input("Enter the first length: "))
    y = float(input("Enter the second length: "))
    z = float(input("Enter the third length: "))

    print(is_valid_triangle(x, y, z))


if __name__ == "__main__":
    main()
