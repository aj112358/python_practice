# Exercise 183: Element Sequences
# Next element in the sequence begins with last letter
# of the previous element.
# Element sequences cannot contain duplicates!
# SINGLE PLAYER: Find longest sequence.
# TWO PLAYER: Mess up your opponent.

from string import ascii_uppercase


ELEMENTS = {x: [] for x in list(ascii_uppercase)}
# ELEMENTS = []
with open("elements.txt", mode="r") as file:

    lines = file.readlines()
    for line in lines:
        x = line.rfind(",")
        name = line[x+1:].strip()
        ELEMENTS[name[0]].append(name)
        # ELEMENTS.append(name)
    print(ELEMENTS)


def longest_sequence(element: str, pool: dict = ELEMENTS) -> list:

    if element == "":
        return []

    next_letter = element[-1].capitalize()
    best_so_far = []

    for item in ELEMENTS[next_letter]:

        next_element = item[-1].capitalize()
        ELEMENTS[next_letter].remove(item)
        candidate_list = longest_sequence(next_element)
        # if item in candidate_list:
        #     continue
        if len(candidate_list) > len(best_so_far):
            best_so_far = candidate_list

    return [element] + best_so_far


def main():
    first = input("Starting element: ").capitalize()
    while first not in ELEMENTS[first[0]]:
        first = input("Must enter a valid element! ").capitalize()
    ELEMENTS[first[0]].remove(first)
    result = longest_sequence(first)
    print(result)


main()
