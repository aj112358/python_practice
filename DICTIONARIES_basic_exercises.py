# Exercise 136: Reverse Lookup

def reverse_lookup(d: dict, value) -> list:
    """Find keys in a dictionary associated to some value."""

    keys = []

    for k, v in d.items():
        if v == value:
            keys.append(k)

    return keys


def main():
    my_dict = {"a": 1, "b": 2, "c": 3, "d":1 }
    value = 1
    keys = reverse_lookup(my_dict, value)
    print(keys)


if __name__ == "__main__":
    main()


# Exercise 140: Postal Code
# Trivial

# Exercise 145: Scrabble Scores
# Trivial

