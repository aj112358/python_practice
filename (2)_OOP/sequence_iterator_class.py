"""An class that provides iteration for ANY Python sequence type, taken from the book.

Created By: AJ Singh
Date: Feb 10, 2021
"""


class SequenceIterator:
    """An iterator for ANY of Python's sequence types."""

    def __init__(self, sequence):
        """Creates an iterator for the given sequence."""
        self._seq = sequence  # Keep a reference to the original sequence.
        self._k = -1          # Will increment to 0 on the FIRST call to "next"

    def __next__(self):
        """Return the next element, or raise StopIteration error."""

        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def __len__(self):
        return len(self._seq)

    def __eq__(self, other):
        """Determine whether two sequences are equal element-wise."""

        # if len(self) != len(other):
        #     return False
        #
        # for k in range(len(self)):
        #     # if self.__next__() != other.__next__():
        #     #     return False
        #     if self._seq[k] != other._seq[k]:
        #         return False

        # return True

        return self._seq == other._seq

    def __lt__(self, other):
        """Determine whether one sequence is less than another lexicographically."""
        return self._seq < other._seq


if __name__ == "__main__":
    x = "a b c d".split()
    print(x)

    x_iterator = SequenceIterator(x)
    print(x_iterator)

    print(x_iterator.__next__())
    x_iterator.__next__()
    print(x_iterator.__next__())
    print(x_iterator.__next__())

    # print(x_iterator.__next__())


    y = "w x y z".split()
    print(y)

    y_iterator = SequenceIterator(y)

    print(next(y_iterator))
    print(next(y_iterator))
    print(next(y_iterator))
    print(next(y_iterator))

    print(len(x_iterator))

    z = "a b c d". split()
    z_iterator = SequenceIterator(z)

    print(x_iterator == z_iterator)
    print(x_iterator == y_iterator)



