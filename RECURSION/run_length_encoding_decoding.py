# Exercise 185 & 186: Run-Length Encoding & Decoding

# Input is a 'run-length compressed' list.
def decompress(data: list) -> list:

    if len(data) < 2:
        return []
    return [data[0]]*data[1] + decompress(data[2:])


def compress(data) -> list:

    if len(data) == 0:
        return []

    length = 1
    while length < len(data) and data[length] == data[0]:
        length += 1
    return [data[0]] + [length] + compress(data[length:])


def main():

    z = "AAAAABBBCCDEEE"
    result2 = compress(z)
    print(result2)

    y = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
         'B', 'B', 'B', 'B', 'C', 'C', 'A', 'A', 'A', 'A', 'A', 'A',
         'B', 'B', 'B', 'B', 'B']
    result1 = compress(y)
    print(result1)

    x = ["A", 12, "B", 4, "A", 6, "B", 2]
    result = decompress(x)
    print(result)


main()
