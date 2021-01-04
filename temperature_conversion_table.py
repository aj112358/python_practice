# Exercise 65: Temperature Conversion Table

from tabulate import tabulate

HEADINGS = ["Celsius", "Fahrenheit"]
DATA = [ [c, round(c*9/5+32, 2)] for c in range(0,110,10) ]

print(tabulate(DATA, HEADINGS, tablefmt="grid"))