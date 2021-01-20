# Exercise 184: Flatten a List

def flatten(data: list) -> list:

    if len(data) == 0:
        return []

    if type(data[0]) is list:
        list1 = flatten(data[0])
    else:
        list1 = [data[0]]

    list2 = flatten(data[1:])

    return list1 + list2


def main():
    x = [[0], 1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    result = flatten(x)
    print(result)


main()
