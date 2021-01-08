# This program converts a text message into the buttons you would press on an old cell phone.
# Created By: AJ Singh
# Date: Jan 8, 2021

from string import ascii_uppercase

ALPHABET = ascii_uppercase
SYMBOLS = list(".,?!:")





def create_keypad():
    """Generate old cell phone keypad mappings."""

    phone = { letter:0 for letter in ALPHABET }

    mod = 0
    num = 0
    for key in phone:
        phone[key] = num+2

        if key == "R" or key == "Y":
            continue
        else:
            mod += 1

        if mod == 3:
            mod = 0
            num += 1

    phone[" "] = 0

    for _ in SYMBOLS:
        phone[_] = 1

    return phone


# phone = create_keypad()


phone = {1: list(".,?!:"),
         2: list("ABC"),
         3: list("DEF"),
         4: list("GHI"),
         5: list("JKL"),
         6: list("MNO"),
         7: list("PQRS"),
         8: list("TUV"),
         9: list("WXYZ"),
         0: list(" ")}

#
def generate_key_strokes(message: str) -> str:
    """Convert text message to actual button presses."""

    converted = ""
    message = message.upper()

    for letter in message:
        for key in phone:
            if letter in phone[key]:
                converted += str(key) * (phone[key].index(letter)+1)

    return converted




def main():

    message = input("Enter text message to convert: ")
    conversion = generate_key_strokes(message)
    print(conversion)


if __name__ == '__main__':
    main()
