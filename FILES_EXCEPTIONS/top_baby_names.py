# Exercise 163: Names that Reached Number One

import os

cwd = os.getcwd()
directory_name = os.path.join(cwd, "BabyNames")
files = os.listdir(directory_name)

boys, girls = [], []
for index, file in enumerate(files):
    file_path = os.path.join(directory_name, file)

    with open(file_path, mode="r") as boom:
        name = boom.readline().split()[0]

        if index % 2 == 0 and name not in boys:
            boys.append(name)
        if index % 2 == 1 and name not in girls:
            girls.append(name)

print("The most popular boy names are: ", *boys, sep="\n")
print("\nThe most popular girl names are: ", *girls, sep="\n")
