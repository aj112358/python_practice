# Exercise 176: The NATO Phonetic Alphabet

from string import ascii_lowercase

NATO = {
    'a': "Alpha",
    'b': "Bravo",
    'c': "Charlie",
    'd': "Delta",
    'e': "Echo",
    'f': "Foxtrot",
    'g': "Golf",
    'h': "Hotel",
    'i': "India",
    'j': "Juliet",
    'k': "Kilo",
    'l': "Lima",
    'm': "Mike",
    'n': "November",
    'o': "Oscar",
    'p': "Papa",
    'q': "Quebec",
    'r': "Romeo",
    's': "Sierra",
    't': "Tango",
    'u': "Uniform",
    'v': "Victor",
    'w': "Whisky",
    'x': "XRay",
    'y': "Yankee",
    'z': "Zulu",
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine"}


# Display a word in NATO phonetic spelling.
def phonetic_spelling(word: str):

    if word == "":
        return ""

    tail = word[1:]

    if word[0].lower() in set(ascii_lowercase):
        char = NATO[word[0].lower()]
        return char + " " + phonetic_spelling(tail)

    return phonetic_spelling(tail)


to_convert = input("Enter a word to convert: ")
phonetic = phonetic_spelling(to_convert)
print(phonetic)
