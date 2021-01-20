# Exercise 77: Multiplication Table

from tabulate import tabulate

num = int(input("What multiple? "))

HEADERS = [] + list(range(1,num+1))
ROWS = [ [i]+[i*j for j in range(1,num+1) ] \
         for i in range(1,num+1)   ]

print(tabulate(ROWS, HEADERS))

