# Exercise 160: Weird Words
# cie -> no
# cei -> yes
# c*ie -> yes
# c*ei -> no


def open_file():

    try:
        file = open("words.txt", mode="r")
        return file
    except FileNotFoundError:
        print("File not found. Try again.")
        quit()


def check_ie_rule(words):

    yes = open("follows_ie.txt", mode="w")
    no = open("follows_ie_false.txt", mode="w")

    # Work one after the other
    rules = {"cie": False,
             "cei": True,
             "ie": True,
             "ei": False}

    for word in words:

        if "cie" in word:
            no.write(word+"\n")
        elif "cei" in word:
            yes.write(word+"\n")
        elif "ie" in word:
            yes.write(word+"\n")
        elif "ei" in word:
            no.write(word+"\n")

    yes.close()
    no.close()


def print_results():
    pass



def main():
    file_obj = open_file()
    lines = file_obj.readlines()
    lines = [line.strip() for line in lines]

    words = []
    for line in lines:
        x = line.split()
        words.extend(x)

    # words = [line.split() for line in lines]
    check_ie_rule(words)

    # print(words)


main()
