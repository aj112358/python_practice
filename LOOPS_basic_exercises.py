# Exercise 63: Average

count = 0
total = 0
n = int(input("Enter a value (0 to quit): "))

if n == 0:
    print("Cannot start with a 0!")
else:
    while n != 0:
        count += 1
        total += n
        n = int(input("Enter a value (0 to quit): "))

avg = total/count

print("The average is:", avg)

# Exercise 64: Discount Table

ORIGINAL = [4.95, 9.95, 14.95, 19.95, 24.95]

print("Original     Discount     Sale")
for price in ORIGINAL:
    print(price, round(price*0.60, 2), round(price*0.40, 2))

# Exercise 66: No More Pennies
# Trivial

# Exercise 67: Compute the Perimeter of a Polygon
# Trivial

# Exercise 68: Compute a GPA
# Trivial

# Exercise 69: Admission Price

age = input("Enter an age: ")
babies = kids = seniors = adults = 0

while age != "":
    age = int(age)
    if age <= 2:
        babies += 0
    elif age <= 12:
        kids += 14.00
    elif age <= 64:
        adults += 23.00
    elif age >= 65:
        seniors += 18.00

    age = input("Enter an age: ")

total = babies + kids + adults + seniors
print("Total cost: $%.2f" % total)

# Exercise 70: Parity Bits
# Trivial

# Exercise 71: Approximate pi

num_terms = 1
appx = int(input("How many approximations: "))

while num_terms <= appx:
    result = 3

    for i in range(1, num_terms):
        result += (-1)**(i+1) * 4/( (2*i)*(2*i+1)*(2*i+2) )

    print(result)
    num_terms += 1

# Exercise 72: Fizz-Buzz

n = int(input("Highest number: "))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 74: Square Root
# Trivial

# Exercise 75: Is a String a Palindrome

my_string = input("Gimme a string: ")
the_length = len(my_string)

for i in range(the_length):
    if my_string[i] != my_string[the_length-i-1]:
        print("NOT a palindrome!")
        break

if i == the_length-1:
    print("IS a palindrome!")

# Exercise 76: Multiple Word Palindromes
# Trivial

# Exercise 78: The Collatz Conjecture
# Trivial

# Exercise 79: Greatest Common Divisor
# Trivial (there is definitely a better algorithm to use than the one given!)

# Exercise 80: Prime Factors
# Trivial (a terrible prime factorization algorithm!)

# Exercise 81: Binary to Decimal
# Trivial

# Exercise 82: Decimal to Binary
# Trivial








































































