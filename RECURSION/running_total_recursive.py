# Exercise 173: Total the Values


def running_total():

    x = input("Number: ")

    if x == "":
        return 0.0
    else:
        return float(x) + running_total()


total_sum = running_total()
print("Total sum:", total_sum)
