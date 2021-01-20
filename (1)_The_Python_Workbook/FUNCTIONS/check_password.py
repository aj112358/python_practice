####
# This program determines whether a password is good based on the criteria:
#   - At least 8 characters long
#   - Has at least one uppercase letter
#   - Has at least one lowercase letter
#   - Has at least one digit
# Created by: AJ Singh
# Date: January 5, 2020

# Check an input string against password criteria.
# @param password: Input string to check.
# @return: True if criteria passed; false otherwise.
def is_good_password(password: str) -> bool:
    """Check whether a password satisfies the following criteria:
        - at least 8 characters long
        - contains at least one uppercase letter
        - contains at least one lowercase letter
        - contains at least one number"""

    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    i = 0
    while not (has_upper and has_lower and has_digit):
        if password[i].isupper():
            has_upper = True
        if password[i].islower():
            has_lower = True
        if password[i].isdigit():
            has_digit = True

        i += 1
        if i == len(password):  # Looped through entire string
            break

    return has_upper and has_lower and has_digit


def main():
    password = input("Please enter a potential password: ")

    if is_good_password(password):
        print("This string satisfies the criteria for a password.")
    else:
        print("You should consider a different password!")


if __name__ == "__main__":
    main()
