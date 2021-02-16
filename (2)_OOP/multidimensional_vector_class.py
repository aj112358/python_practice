"""An implementation of geometric vectors, taken from the book.

Created By: AJ Singh
Date: Feb 10, 2021
"""


class Vector:
    """Represent a vector in a multi-dimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of a vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the j-th component of a vector."""
        return self._coords[j]

    def __setitem__(self, j, value):
        """Set the j-th component of a vector to value."""
        self._coords[j] = value

    def __add__(self, other):
        """Return sum of two Vector instances."""

        if len(self) != len(other):
            raise ValueError("Vectors must be of same dimension.")

        result = Vector(len(self))  # New vector to store sum.
        for j in range(len(self)):
            result[j] = self[j] + other[j]

        return result

    def __eq__(self, other):
        """Return True if two Vector instances have same components."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if two Vector instances differ at some component."""
        return not (self == other)  # Relies on __eq__ defined above!

    def __str__(self):
        """Produces string representation of a Vector instance."""
        return '<' + str(self._coords)[1:-1] + '>'

    # My addition for dot product
    def __mul__(self, other):
        """Return dot product of two Vector instances."""

        if len(self) != len(other):
            raise ValueError("Vectors must have same dimension.")

        result = 0
        for j in range(len(self)):
            result += self[j] * other[j]

        return result

    # My addition for scalar multiplication
    def scale(self, c: (int, float)):
        """Returns scalar multiple of a Vector instance."""

        if not isinstance(c, (int, float)):
            raise TypeError("Scale value c must be a number.")

        result = Vector(len(self))
        for j in range(len(self)):
            # self[j] *= c
            result[j] = self[j] * c

        return result
        # return self


if __name__ == "__main__":
    u = Vector(4)
    v = Vector(4)

    u[0], u[1], u[2], u[3] = 1, 2, 3, 4
    v[0], v[1], v[2], v[3] = 5, 6, -7, -1
    print(u)
    print(v)

    w = u + v
    print(w)

    print(u == v)
    print(u is v)

    print(u * v)
    print(v * u)

    print(u.scale(2.1))
    print(u)

    # print(v.scale("hello"))