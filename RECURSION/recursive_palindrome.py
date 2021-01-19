# Exercise 178: Recursive Palindrome


# Check if a string is a palindrome using recursion.
def is_palindrome(string: str):

    string = string.lower()

    if len(string) in {0, 1}:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


to_check = input("String to check if palindrome: ")
print(is_palindrome(to_check))
