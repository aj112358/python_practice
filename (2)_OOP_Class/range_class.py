"""An implementation of Python's range function, taken from book.

Created By: AJ Singh
Date: Feb 10, 2021
"""


class MyRangeClass:
    """A class that mimics Python's built-in range function."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Has similar function signature to actual range class.
        """

        if step == 0:
            raise ValueError("Step must be a positive integer.")

        if stop is None:
            start, stop = 0, start  # Effectively making range(0,start)

        # Pre-computing number of values
        self._length = max(0, (stop - start + step - 1)//step)

        # These will support __getitem__ below.
        self._start = start
        self._step = step

    def __len__(self):
        """Return the number of values in the range."""
        return self._length

    def __getitem__(self, k):
        """Return the value at k-th index."""

        # Converting negative indices
        if k < 0:
            k += len(self)

        if not (0 <= k < self._length):
            raise IndexError("Index out of range.")

        return self._start + k * self._step


if __name__ == "__main__":
    r = MyRangeClass(5)
    print(r)

    for i in r:
        print(i, end=" - ")

    print()
    for i in MyRangeClass(10, 0, -3):
        print(i, end=" - ")
