"""An implementation of the keyword argument 'key=' used in Python's built-in sorting functions, taken from book.

An illustration of the 'decorate-sort-undecorate' design pattern.

Created By: AJ Singh
Date: March 29, 2021
"""


from merge_sort import merge_sort


# class SortingDecorator:

class _Item:
    """Lightweight composite to store key-value pairs."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __lt__(self, other):
        return self._key < other._key


def decorated_merge_sort(data, key=None):
    """Demonstration of the 'decorate-sort-undecorate' design pattern."""

    if key is not None:
        for j in range(len(data)):
            data[j] = _Item(k=key(data[j]), v=data[j])

    merge_sort(data)

    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value
