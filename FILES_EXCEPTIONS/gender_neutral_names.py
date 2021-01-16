# Exercise 164: Gender Neutral Names
# Determine all names that were used for both boys and girls.

import os
year = input("What year? ")
FILE_EXT = ["_BoysNames.txt", "_GirlsNames.txt"]

cwd = os.getcwd()
directory_name = os.path.join(cwd, "BabyNames")
file_paths = [os.path.join(directory_name, year+x) for x in FILE_EXT]

for index, file in enumerate(file_paths):

    with open(file, mode="r") as data:
        lines = data.readlines()
        names = set(map(lambda x: x.strip().split()[0], lines))

        if index % 2 == 0:
            boys = names.copy()
        else:
            girls = names.copy()

common_names = boys.intersection(girls)
if not len(common_names):
    print("There were no gender neutral names used in", year)
else:
    print(f"The gender neutral names in {year} were:", *common_names, sep="\n")
