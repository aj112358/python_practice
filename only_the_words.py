#### This programs splits a sentence into individual words.
# Created By: AJ Singh
# Date: Jan 6, 2021

PUNCTUATION = list(",.?-'!:;")


# Function to extract words from a sentence
# (does not remove word-interior punctuations).
# @param sentence: The string you wish to split.
# @return: List of individual words
def extract_words(sentence: str) -> list:
    """Creates list of all words in a string."""

    splits = sentence.split()
    words = []

    for split in splits:
        if split[0] in PUNCTUATION and split[-1] in PUNCTUATION:
            words.append(split[1:-1])
        elif split[0] in PUNCTUATION and split[-1] not in PUNCTUATION:
            words.append(split[1:])
        elif split[0] not in PUNCTUATION and split[-1] in PUNCTUATION:
            words.append(split[:-1])
        else:
            words.append(split)

    return words


def main():
    string = input("String you wish to split: ")
    words = extract_words(string)
    print("Here are the words:\n", words)


if __name__ == "__main__":
    main()
