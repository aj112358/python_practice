# Exercise 110: Sorted Order

integer_array = []

n = int(input("Please enter an integer (0 to quit):"))

while n != 0:
    integer_array.append(n)
    n = int(input("Please enter an integer (0 to quit):"))

integer_array.sort()

print("Here are your values in increasing order:\n")
for _ in range(len(integer_array)):
    print(integer_array[_])


# Exercise 111: Reverse Order

integer_array = []

n = int(input("Please enter an integer (0 to quit):"))

while n != 0:
    integer_array.append(n)
    n = int(input("Please enter an integer (0 to quit):"))

integer_array.sort(reverse=True)

print("Here are your values in decreasing order:\n")
for _ in range(len(integer_array)):
    print(integer_array[_])


# Exercise 112: Remove Outliers

def remove_outliers(data: list, n: int) -> list:

    fixed_list = sorted(data)
    return fixed_list[n:len(fixed_list)-n]

def main():
    print("Please enter a list:")
    user_list = input().split()

    if len(user_list) < 4:
        print("You list must have at least 4 elements.")
        quit()

    n = int(input("What outliers do you want to remove: "))

    if n < 0:
        print("Invalid n value.")
        quit()

    print("Your list is:\n", user_list)
    user_list.sort()
    print("Sorted:\n", user_list)
    new_list = remove_outliers(user_list, n)
    print("Outliers removed:\n", new_list)

if __name__ == "__main__":
    main()

# Exercise 113: Avoiding Duplicates

word = input("Enter a word: ")
words_list = []

while word != "":
    if word not in words_list:
        words_list.append(word)

    word = input("Enter a word: ")

print("Here are the unique words:")
for _ in words_list:
    print(_)

# Exercise 114: Negatives, Zeros, Positives

positive_array = []
zero_array = []
negative_array = []

n = input("Please enter an integer (blank line to quit):")
while n != "":

    n = int(n)
    if n > 0:
        positive_array.append(n)
    elif n == 0:
        zero_array.append(n)
    else:
        negative_array.append(n)

    n = input("Please enter an integer (blank line to quit):")

for num in negative_array:
    print(num)
for num in zero_array:
    print(num)
for num in positive_array:
    print(num)


# Exercise 119: Below and Above Average
# Trivial

# Exercise 120: Formatting a List
# Trivial

# Exercise 121: Random Lottery Numbers
# Trivial (just use 'random.sample()' !!!)


# Exercise 124: Line of Best Fit
# Trivial

# Exercise 127: Check if List is Sorted
# Trivial






























































