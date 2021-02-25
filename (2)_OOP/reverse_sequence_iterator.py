"""A class that provides REVERSE sequence iteration.

Created By: AJ Singh
Date: Feb 24, 2021
"""

from sequence_iterator_class import SequenceIterator


class ReverseIterator(SequenceIterator):
    """Class to iterate a sequence in reverse."""

    def __init__(self, sequence):
        super().__init__(sequence)
        self._seq = sequence[::-1]


if __name__ == "__main__":

    x = "a b c d".split()
    x_iterator = ReverseIterator(x)

    print(next(x_iterator))
    print(next(x_iterator))
    print(next(x_iterator))
    print(next(x_iterator))
