"""An example of creating our own version of collections.Sequence ABC, taken from book.

Created By: AJ Singh
Date: Feb 13, 2021
"""

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of 'collections.Sequence' ABC."""

    @abstractmethod
    def __len__(self):
        """Return the length of a sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return 'True' if val found in sequence; False otherwise."""

        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return first (left-most) index at which 'val' is found, or raise ValueError."""

        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("Value not in sequence.")

    def count(self, val):
        """Return the number of elements equal to given value."""

        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
