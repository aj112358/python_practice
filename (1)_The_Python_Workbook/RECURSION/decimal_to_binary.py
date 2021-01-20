# Exercise 175: Decimal to Binary


def dec_to_bin(n: str):

    if n == '0':
        return "0"
    if n == '1':
        return "1"
    if int(n) < 0:
        print("Positive numbers only!!!!")
        quit()

    r = int(n) % 2
    d = int(n) // 2

    return dec_to_bin(str(d)) + str(r)


decimal = input("Enter a decimal number to convert: ")
binary = dec_to_bin(decimal)

print("The binary representation is:", binary)