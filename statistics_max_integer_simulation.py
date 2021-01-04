# Exercise 83: Maximum Integer

from random import randint


def integer_sampling():

    current_max = randint(1, 100)
    # print("FirstNo: ", current_max)
    update = 0

    for _ in range(99):
        n = randint(1, 100)

        if n > current_max:
            current_max = n
            update += 1
            # print("Integer: ", n, " <--UPDATE", update)
        # else:
            # print("Integer: ", n)

    # print("Max value encountered:", current_max)
    # print("Number of updates: ", update, "\n")

    return update


total = 0
SAMPLES = 1000000
for _ in range(SAMPLES):
    sum += integer_sampling()

print(total)
print("Expected value of updates: ", round(total/SAMPLES, 2))
