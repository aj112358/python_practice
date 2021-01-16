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

        #### 3872 = yes
        #### 2763 = no
        # Skip any word not containing "ei" or "ie"
        if "ei" not in word and "ie" not in word:
            continue

        # Only need to check for "cie"
        # Otherwise, having "ie" is fine.
        if "cie" in word:
            no.write(word+"\n")
            continue

        # Now it remains to investigate "cei" and "ei"
        index = word.find("ei")
        if index == -1:  # There is no "ei"
            yes.write(word+"\n")
            continue

        while index != -1:  # There is at least one "ei"
            if word[index-1] != "c":
                no.write(word+"\n")
                break
            else:  # Check remainder of word
                index = word[index+1:].find("ei")
        else:  # There is no "ei" without "c" before it.
            yes.write(word+"\n")





        #### 3868 = yes
        #### 2735 = no
        # if "ie" in word or "ei" in word:
        #
        #     if "ie" in word and "ei" not in word:
        #         if "cie" in word:
        #             no.write(word+"\n")
        #         else:
        #             yes.write(word+"\n")
        #
        #     if "ie" not in word and "ei" in word:
        #         if "cei" in word:
        #             yes.write(word+"\n")
        #         else:
        #             no.write(word+"\n")



        #### 4157 = yes
        #### 2735 = no
        # if "cie" in word:
        #     no.write(word + "\n")
        # if "ie" in word:
        #     yes.write(word+"\n")
        # elif "cei" in word:
        #     yes.write(word+"\n")
        # elif "ei" in word:
        #     no.write(word+"\n")

        #### 3713 = yes
        #### 3366 = no
        # if "ie" in word or "cei" in word:  # Its good so far!
        #     if "cie" in word or "ei" in word:
        #         no.write(word+"\n")
        #     else:
        #         yes.write(word+"\n")
        #
        # if "cie" in word or "ei" in word:
        #     no.write(word+"\n")

        #### 3900 = yes
        #### 2735 = no
        # if "cie" in word:
        #     no.write(word + "\n")
        # elif "ie" in word:
        #     yes.write(word+"\n")
        # elif "cei" in word:
        #     yes.write(word+"\n")
        # elif "ei" in word:
        #     no.write(word+"\n")



        #### 233002 = yes
        #### 2922 = no
        #
        # if "ie" in word:
        #     boom = True
        # if "cie" in word:
        #     boom = False
        #
        # if "ei" in word:
        #     boom = False
        # if "cei" in word:
        #     boom = True
        #
        #
        # if boom:
        #     yes.write(word+"\n")
        # else:
        #     no.write(word+"\n")



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
