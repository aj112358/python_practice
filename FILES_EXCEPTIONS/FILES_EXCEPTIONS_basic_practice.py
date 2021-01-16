# Exercise 157: Both Letter Grades and Grade Points
# Trivial

# Exercise 165: Most Births in a given time period
# Trivial - Just wanted to see how to get all the file names.
# Can also import function from Exercise 163
import os

year_start = int(input("What start year? "))
year_end = int(input("What end year? "))

FILE_EXT = ["_BoysNames.txt", "_GirlsNames.txt"]

cwd = os.getcwd()
directory_name = os.path.join(cwd, "BabyNames")
file_paths = [os.path.join(directory_name, str(year)+x) \
              for x in FILE_EXT for year in range(year_start, year_end+1)]

print(file_paths)

# Exercise 166: Distinct Names
# Trivial/I already did this (just use set data structure)
