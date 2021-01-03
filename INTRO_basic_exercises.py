# Exercise 1: Mailing Address

print("First Last")
print("123 Some Rd")
print("City State Zipcode")

# Exercise 2: Hello

name = input("What is your name? ")
print("Hello,", name, "!")
print(f"Hello, {name}!")

# Exercise 3: Area of a Room

#width = float(input("Please enter the width (in meters): "))
#length = float(input("Please enter the length (in meters): "))

width, length = map(float, input("Please enter the width and length of the room (in meters), respectively: ").split())
print(f"The area of this room is {width*length}")

# Exercise 4: Area of a Field

length = float(input("What is the length (in feet): "))
width = float(input("What is the width (in feet): "))

ACRE_TO_FEET = 43560 # Multiplicative!

area = (length * width) / ACRE_TO_FEET

print("The area of your field is %.2f acres." % area)

# Exercise 5: Bottle Deposits

SMALL_DEPOSIT = 0.10
LARGE_DEPOSIT = 0.25

num_small = int(input("How many small containers (1 L or less) do you have: "))
num_large = int(input("How many large containers (more than 1 L) do you have: "))

total_refund = num_large*LARGE_DEPOSIT + num_small*SMALL_DEPOSIT

print("Your total refund will be $%.2f." % total_refund)

# Exercise 6: Tax and Tip

meal_cost = float(input("How much was your meal? "))
TAX_RATE = 0.05
TIP_RATE = 0.18

tax_amount = meal_cost * TAX_RATE
tip_amount = meal_cost * TIP_RATE

total_amount = meal_cost + tip_amount + tax_amount

print("You will pay $%.2f in taxes and $%.2f in tips for a grand total of $%.2f!" % (tax_amount, tip_amount, total_amount ))

# Exercise 7: Sum of N integers

n = int(input("Enter a positive integer: "))
sum = int(n*(n+1)/2)

print(f"The sum of the first {n} integers is: {sum}")

# Exercise 8: Widgets and Gizmos

num_gizmos = int(input("How many gizmos: "))
num_widgets = int(input("How many widgets: "))

WEIGHT_WIDGET = 75
WEIGHT_GIZMO = 112

total_weight = num_gizmos*WEIGHT_GIZMO + num_widgets*WEIGHT_WIDGET

print("The total weight of all parts is %.2f grams" % total_weight)

# Exercise 9: Compound Interest

INTEREST_RATE = 0.04 # per annum

principal = float(input("What was the initial deposit: "))

print("The amount after year one is: $%.2f" % (principal*(1+INTEREST_RATE)))
print("The amount after year two is: $%.2f" % (principal*(1+INTEREST_RATE)**2))
print("The amount after year three is: $%.2f" % (principal*(1+INTEREST_RATE)**3))

# Exercise 10: Arithmetic

from math import log10
a, b = map(int, input("Please enter two integers: ").split())

sum = a+b
difference = a-b
product = a*b
quotient = a//b
remainder = a%b
log_base10 = log10(a)
power = a**b

print("The sum is: ", sum)
print("The difference is: ", difference)
print("The product is: ", product)
print("The quotient of a/b is: ", quotient)
print("The remainder of a/b is: ", remainder)
print("The base-10 logarithm of 'a' is: ", log_base10)
print("The power a^b is: ", power)

# Exercise 11: Fuel Efficiency
# Trivial

# Exercise 12: Distance Between Two Points on Earth

from math import radians, acos, cos, sin

#TO_RADS = lambda x: radians(float(x))
t1, g1 = map(lambda x: radians(float(x)), input("Enter the latitude and longitude of the first point (in degrees): ").split())
t2, g2 = map(lambda x: radians(float(x)), input("Enter the latitude and longitude of the second point (in degrees): ").split())

d = 6371.01 * acos(sin(t1)*sin(t2) + cos(t1)*cos(t2)*cos(g1-g2))

print("The distance between the two locations is %.2f km." % d)

# Exercise 14: Height Units
# Trivial

# Exercise 15: Distance Units
# Trivial

# Exercise 16: Area and Volume
# Trivial

# Exercise 17: Heat Capacity
# Trivial

# Exercise 18: Volume of a Cylinder
# Trivial

# Exercise 19: Free Fall
# Trivial

# Exercise 20: Ideal Gas Law
# Trivial

# Exercise 21: Area of a Triangle
# Trivial

# Exercise 22: Area of a Triangle (Heron's Formula)
# Trivial

# Exercise 23: Area of a Regular Polygon

from math import tan, pi
n = int(input("How many sides in your polygon: "))
s = float(input("What is the side length: "))

area = n*s**2 / (4*tan(pi/n))

print("The area of the polygon is %.2f" % area )

# Exercise 24: Units of Time
# Trivial

# Exercise 25: Current Time

from time import asctime

print(asctime())

# Exercise 27: When is Easter?
# Trivial

# Exercise 28: Body Mass Index
# Trivial

# Exercise 29: Wind Chill
# Trivial

# Exercise 30: Celsius to Fahrenheit and Kelvin
# Trivial

# Exercise 31: Units of Pressure
# Trivial

# Exercise 32: Sum of the Digits in an Integer

number = int(input("Please enter a four-digit integer: "))

a = number // 1000
b = (number % 1000) // 100
c = (number % 100) // 10
d = (number % 10)

sum = a+b+c+d

print(f"The sum of the digits is: {sum}")

# Exercise 34: Day Old Bread

ORIGINAL_PRICE = 3.49
DISCOUNT_RATE = 0.60

num_loaves = int(input("How many loaves of day-old bread are you buying: "))

regular_price = (ORIGINAL_PRICE*num_loaves)
discount = (ORIGINAL_PRICE*num_loaves*DISCOUNT_RATE)

print("Regular price: $%5.2f" % regular_price)
print("Discount:      $%5.2f" % discount)
print("Total:         $%5.2f" % (regular_price-discount))

