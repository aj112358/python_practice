# This program checks if one list is a sublist of another.
# Created By: AJ Singh
# Date: Jan 7, 2021


# Check if a list is a sublist of another list
# @param small: List to check.
# @param large: List to compare with.
# @return: Boolean result.
def is_sublist(small: list, large: list) -> bool:
    """Check if <small> is a sublist of <large>."""

    if not small:  # Checking empty list
        return True

    # Checking if small list is subset of large list
    if not set(small).issubset(set(large)):
        return False

    i = large.index(small[0])
    k: int = 0
    while k < len(small):
        if large[i] != small[k]:
            return False
        k += 1
        i += 1

    return True


def main():
    smaller = list(map(int, input("Enter the smaller list: ").split()))
    larger = list(map(int, input("Enter the larger list: ").split()))
    print(is_sublist(smaller, larger))


if __name__ == '__main__':
    main()
