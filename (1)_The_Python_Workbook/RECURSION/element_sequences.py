# Exercise 183: Element Sequences
# Next element in the sequence begins with last letter
# of the previous element.
# Element sequences cannot contain duplicates!
# SINGLE PLAYER: Find longest sequence.
# TWO PLAYER: Mess up your opponent.

from string import ascii_uppercase


# ELEMENTS = {x: [] for x in list(ascii_uppercase)}
ELEMENTS = []
with open("elements.txt", mode="r") as file:

    lines = file.readlines()
    for line in lines:
        x = line.rfind(",")
        name = line[x+1:].strip()
        # ELEMENTS[name[0]].append(name)
        ELEMENTS.append(name)
    print(ELEMENTS)


def longest_sequence(element: str, selection_pool: list) -> list:

    if element == "":
        return []

    next_letter = element[-1].capitalize()
    best_so_far = []

    for index, item in enumerate(selection_pool):

        if item[0].capitalize() == next_letter:

            candidate_list = longest_sequence(item, selection_pool[:index] + selection_pool[index+1:])

            if len(candidate_list) > len(best_so_far):
                best_so_far = candidate_list

    return [element] + best_so_far


def main():
    first = input("Starting element: ").capitalize()
    while first not in ELEMENTS:
        first = input("Must enter a valid element! ").capitalize()
    ELEMENTS.remove(first)
    result = longest_sequence(first, ELEMENTS)
    print(*result, sep="\n")


main()
