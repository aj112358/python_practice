# Convert an English sentence to Morse code.
# Created By: AJ Singh
# Date: Jan 8, 2021


MORSE = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
          'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
          'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
          'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
          'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
          '1':'.----', '2':'..---', '3':'...--',
          '4':'....-', '5':'.....', '6':'-....',
          '7':'--...', '8':'---..', '9':'----.',
          '0':'-----', ', ':'--..--', '.':'.-.-.-',
          '?':'..--..', '/':'-..-.', '-':'-....-',
          '(':'-.--.', ')':'-.--.-' }


# Encodes to Morse code.
# @param message: String to translate.
# @return: Morse code translation.
def to_morse_code(message: str) -> str:
    """Convert an English sentence into Morse code."""

    message = message.upper()
    converted = ""

    for letter in message:
        if letter in MORSE:
            converted += MORSE[letter] + " "

    return converted


def main():
    message = input("Enter message to translate to Morse code: ")
    translation = to_morse_code(message)
    print(translation)


if __name__ == '__main__':
    main()
