# Exercise 169: Redacting Text in a File
# Redact sensitive words.
# List of sensitive words provided in another file.

import sys

# <Python script> <Original> <Sensitive> <Redacted>
if len(sys.argv) < 4:
    print("Not enough command line arguments. Please try again.")
    quit()


def open_file():
    try:
        file_to_check = open(sys.argv[1], mode="r")
        return file_to_check
    except FileNotFoundError:
        print("File not found. Please try again.")


def get_sensitive_words():

    # with open("test6_sensitive_words.txt", mode="r") as data:
    with open(sys.argv[2], mode="r") as data:
        lines = data.readlines()
        words = set(map(lambda x: x.strip().lower(), lines))

    return words


def redact(text: str, sensitive: set) -> str:

    for word in sensitive:

        index = text.lower().find(word)
        if index != -1:
            text = text[:index] \
                   + text.lower()[index:index+len(word)].replace(word, "*"*len(word)) \
                   + text[index+len(word):]

    return text


def create_redacted_file(data: str):

    with open(sys.argv[3], mode="w") as out_file:
        out_file.write(data)


def main():
    in_file = open_file()
    data = in_file.read()

    sensitive_words = get_sensitive_words()
    redacted_data = redact(data, sensitive_words)
    print("\n")
    print(redacted_data)
    create_redacted_file(redacted_data)

    in_file.close()


main()
