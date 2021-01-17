# Exercise 171: Consistent Line Lengths


MAX_LENGTH = 40


def open_file(file):
    try:
        file_obj = open(file, mode="r")
        return file_obj
    except FileNotFoundError:
        print("Unable to open file.")
        quit()


def construct_paragraphs(lines):
    paragraphs = []
    string = ""
    for line in lines:

        if line != "":
            string = string + " " + line
        else:
            paragraphs.append(string.lstrip())
            paragraphs.append("")
            string = ""
    paragraphs.append(string)
    return paragraphs


def words_from_para(paragraphs):
    words = []
    for para in paragraphs:
        words.append(para.split())
    return words


def print_data(paragraphs):

    for para in paragraphs:
        if not para:  # If it's a new paragraph, print empty line.
            print("")
            continue

        line = ""
        for word in para:

            if len(line+word) < MAX_LENGTH:
                line += " " + word
            else:
                print(line.lstrip())
                line = word
        print(word)  # Prints remaining word(s) if any.


def main():

    file_obj = open_file("test8.txt")
    lines = file_obj.readlines()
    lines = [line.strip() for line in lines]
    # print(lines)

    paragraphs = construct_paragraphs(lines)
    # print(paragraphs)

    words = words_from_para(paragraphs)
    # print(words)
    print_data(words)


main()
