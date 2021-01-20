# Exercise 35: Even or Odd?
# Trivial

# Exercise 36: Dog Years

human_age = float(input("What is your age (in years)? "))

if human_age > 2:
    dog_age = 2*10.5 + (human_age-2)*4
    print("Your age in dog-years is", dog_age)
elif 0<= human_age <=2:
    dog_age = human_age * 10.5
    print("Your age in dog-years is", dog_age)
else:
    print("You entered an invalid age!")

# Exercise 37: Vowel or Consonant

VOWELS = list('aeiou')

letter = input("Please enter a single letter: ")

if letter in VOWELS:
    print("This is a vowel.")
elif letter == 'y':
    print("This is and sometimes is not a vowel.")
else:
    print("This is a consonant.")

# Exercise 38: Name That Shape

shapes = [None, None, None, "Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon"]

num_sides = int(input("How many sides? "))

if num_sides in range(3,11):
    print("Your shape is called a", shapes[num_sides])
else:
    print("Out of range.")


# Exercise 39: Month Name to Number of Days

LONG = ["january", "march", "may", "july", "august", "october", "december"]
SHORT = ["april", "june", "september", "november"]

month = input("Give a month (full name): ").lower()

if month in LONG:
    print(month.capitalize(), "has 31 days.")
elif month in SHORT:
    print(month.capitalize(), "has 30 days.")
else:
    print(month.capitalize(), "has either 28 or 29 days.")

# Exercise 40: Sound Levels
# Trivial

# Exercise 41: Classifying Triangles
# Trivial

# Exercise 42: Note to Frequency
# Trivial

# Exercise 43: Frequency to Note
# Trivial

# Exercise 44: Faces on Money
# Trivial

# Exercise 45: Date to Holiday Name
# Trivial

# Exercise 46: What Color is the Square

FILES = list('abcdefgh')

square_name = input("Enter a chess square name:").lower()

parity = (-1)**(FILES.index(square_name[0])+int(square_name[1]))

if parity == -1:
    print("This square is black.")
elif parity == +1:
    print("This square is white.")
else:
    print("Invalid input.")


# Exercise 48: Birthdate to Astrological Sign
# Same as Exercise 47 (Season from Date)

# Exercise 49: Chinese Zodiac
# Trivial

# Exercise 50: Richter Scale
# Trivial

# Exercise 51: Roots of a Quadratic Function
# Trivial

# Exercise 52: Letter Grade to Grade Points
# Trivial

# Exercise 53: Grade Points to Letter Grade
# Trivial

# Exercise 54: Assessing Employees

MEANINGS = ['Unacceptable', "Acceptable", "Meritorious"]
RAISE_FACTOR = 2400

rating = float(input("What is the employee rating? "))

if rating == 0.0:
    print("The employees rating is unacceptable, with a raise of", RAISE_FACTOR*rating)
elif rating == 0.4:
    print("The employees rating is acceptable, with a raise of", RAISE_FACTOR*rating)
elif rating >= 0.6:
    print("The employees rating is meritorious, with a raise of", RAISE_FACTOR*rating)
else:
    print("Invalid rating entered.")

# Exercise 55: Wavelengths of Visible Light
# Trivial

# Exercise 56: Frequency to Name
# Trivial

# Exercise 57: Is It A Leap Year?

year = int(input("What year is it: "))

if year % 400 == 0:
    print("It is a leap year.")
elif year % 100 == 0:
    print("It is NOT a leap year.")
elif year % 4 == 0:
    print("It is a leap year.")
else:
    print("It is NOT a leap year.")

# Exercise 59: Next Day
# Trivial

# Exercise 60: What day of the week is Jan 1?
# Trivial

# Exercise 61: Is a License Plate Valid?

plate = input("What's the license plate? ").lower()

if len(plate) != 6 or len(plate) != 7:
    print("Invalid license plate.")
elif len(plate) == 6:
    if plate[:3].isalpha() and plate[3:].isdigit():
        print("This is an older license plate.")
    else:
        print("Invalid license plate.")
elif len(plate == 7):
    if plate[:4].isdigit() and plate[4:].isalpha():
        print("This is a new license plate.")
    else:
        print("Invalid license plate.")

# Exercise 62: Roulette Payouts
# Trivial




















