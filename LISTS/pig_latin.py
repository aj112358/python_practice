#### This program converts an English sentence into pig Latin.
# NOTE: 'y' is NOT considered a vowel here.
# Created By: AJ Singh
# Date: Jan 6, 2021

from string import ascii_letters

CONSONANTS = set(ascii_letters).difference(set("aeiouAEIOU"))
PUNCTUATION = list(",.?-'!:;")


# Function to translate a string to pig Latin
# @param sentence: String to translate.
# @return: Translated sentence.
def to_pig_latin(sentence: str) -> str:
    """Convert an English sentence to Pig Latin. (NOTE: The letter 'y' is NOT considered a vowel)"""

    new_sent = ""
    words = sentence.split()

    for word in words:

        if word[0] not in CONSONANTS:  # Word starts with a vowel (a,e,i,o,u)

            if word[-1] in PUNCTUATION:
                new_word = word[:-1] + "yay" + word[-1] + " "
            else:
                new_word = word + "yay "

        else:  # Word starts with a consonant (including 'y'!)

            # Check if the word even has a vowel
            has_vowel = False
            for char in word:
                if char not in CONSONANTS and char not in PUNCTUATION:
                    has_vowel = True

            if has_vowel:

                # Find the first instance of a vowel
                first_vowel = 1
                while word[first_vowel] in CONSONANTS:
                    first_vowel += 1

                if word[-1] in PUNCTUATION:
                    new_word = word[first_vowel:-1] + word[:first_vowel] + "ay" + word[-1] + " "
                else:
                    new_word = word[first_vowel:] + word[:first_vowel] + "ay "

            else:  # Word doesn't have any vowels!
                if word[-1] in PUNCTUATION:
                    new_word = word[-2] + word[:-2] + "ay" + word[-1] + " "
                else:
                    new_word = word[-1] + word[:-1] + "ay "

        # Capitalizing new word if necessary
        if word[0].isupper():
            new_word = new_word.capitalize()

        new_sent += new_word

    return new_sent


def main():
    to_convert = input("Write a sentence to translate:\n")
    result = to_pig_latin(to_convert)
    print("\n", result)


if __name__ == "__main__":
    main()
