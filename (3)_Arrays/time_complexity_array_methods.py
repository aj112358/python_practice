"""This module investigates the time complexity of various array/list methods.

Some of the code is taken from the 'evaluate_append_operation.py' module.

Created By: AJ Singh
Date: Feb 18, 2021
"""


# from dynamic_array_implementation.DynamicArray import append
from time import time
from tabulate import tabulate

from dynamic_array_implementation import DynamicArray
print(dir(DynamicArray))


def compute_average(n, func):
    """Performs n append operations to an empty list, and returns the *average* time taken."""

    data = DynamicArray()
    start = time()

    for k in range(n):
        data.func(None)
    end = time()

    return (end - start) / n


if __name__ == "__main__":

    MAX_SIZE = 4
    SIZES = [f"10^{i}" for i in range(2, MAX_SIZE + 1)]

    array_sizes = [10**i for i in range(2, MAX_SIZE+1)]
    times_taken = [compute_average(n, DynamicArray.append)*(10**6) for n in array_sizes]

    print(tabulate(zip(SIZES, times_taken), ["Size", "Time"]))
