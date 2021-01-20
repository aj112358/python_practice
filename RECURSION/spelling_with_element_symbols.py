# Exercise 182: Spelling with Element Symbols
# Find and display all element spellings of a word

SYMBOLS = {1: [], 2: [], 3: []}
with open("elements.txt", mode="r") as file:

    lines = file.readlines()
    for line in lines:
        first = line.find(",")
        second = line.rfind(",")
        symbol = line[first+1:second]
        SYMBOLS[len(symbol)].append(symbol)
    # print(SYMBOLS)


def spell_elements(word: str, symbols: dict = SYMBOLS) -> str:

    word = word.capitalize()  # NEED TO HAVE THIS IN HERE !!!!!

    if word == "":
        return ""

    if word[:3] in symbols[3]:
        return word[:3] + spell_elements(word[3:])

    elif word[:2] in symbols[2]:
        return word[:2] + spell_elements(word[2:])

    elif word[:1] in symbols[1]:
        return word[:1] + spell_elements(word[1:])

    else:
        return ""


def main():
    word = input("What word to spell: ")
    spelling = spell_elements(word)
    print(f"{word.capitalize()} can be written as: {spelling}")


main()
