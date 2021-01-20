# Exercise 180: String Edit Distance

# The edit distance between two strings is a measure of their
# similarity. The smaller the edit distance, the more similar
# the strings are with regard to the minimum number of insert,
# delete and substitute operations needed to transform one
# string into the other.


def edit_distance(s: str, t: str) -> int:

    if len(s) == 0:
        return len(t)

    elif len(t) == 0:
        return len(s)

    else:
        cost = 0
        if s[-1] != t[-1]:
            cost = 1

        d1 = edit_distance(s[:-1], t) + 1
        d2 = edit_distance(s, t[:-1]) + 1
        d3 = edit_distance(s[:-1], t[:-1]) + cost

        return min(d1, d2, d3)


def main():

    first = input("First string:  ")
    second = input("Second string: ")
    print(f"The edit distance is {edit_distance(first, second)}.")


main()
