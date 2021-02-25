"""An implementation of Python's range function, taken from book.

Created By: AJ Singh
Date: Feb 10, 2021
"""


class MyRangeClass:
    """A class that mimics Python's built-in range function."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Has similar function signature to actual range class.
        NOTE: If step<0, then make sure that start>stop
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

    def __contains__(self, item):
        """Better implementation."""

        if self._step == 1:
            return self._start < item < self._length

        if self._step == -1:
            return self._start - self._length < item < self._start





if __name__ == "__main__":
    r = MyRangeClass(5)
    print(r)

    for i in r:
        print(i, end=" - ")

    print()
    for i in MyRangeClass(10, 0, -3):
        print(i, end=" - ")

    p = MyRangeClass(start=10_000_000, stop=1, step=-1)
    print("\nLength of p:", len(p))

    print()
    print(2 in p)
    print(9_000_000 in p)
