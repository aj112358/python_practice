"""This is a manual implementation of a dynamic array, for pedagogical purposes.

Created By: AJ Singh
Date: Feb 16, 2021
"""

import ctypes


class DynamicArray:
    """A dynamic array class similar to a Python list."""

    def __init__(self):
        """Creates an empty array of default capacity one."""

        self._n = 0                                 # Actual number of elements in the array
        self._capacity = 1
        self._A = self._make_array(self._capacity)  # Creating the low-level array using ctypes module.

    def __len__(self):
        """Return the number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""

        if not 0 <= k < self._n:
            raise IndexError("Invalid index.")
        return self._A[k]

    def append(self, obj):
        """Add an object to the end of the array."""

        # Check if re-sizing is needed (if current array is full; new array is double in size).
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        self._A[self._n] = obj  # Appending object to the end of the array.
        self._n += 1

    def _make_array(self, c):
        """Return a new array with capacity c."""
        return (c * ctypes.py_object)()

    def _resize(self, c):
        """Resize the internal array, _A, to capacity c."""

        B = self._make_array(c)     # Making new low-level array of capacity c.
        for k in range(self._n):
            B[k] = self._A[k]       # Copying current elements into new array.

        self._A = B                 # Changing original identifier to reference new larger array.
        self._capacity = c          # Updating new capacity.
