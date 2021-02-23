"""An implementation of geometric vectors, taken from the book.

Created By: AJ Singh
Date: Feb 10, 2021
"""


class Vector:
    """Represent a vector in a multi-dimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""

        if isinstance(d, int):
            self._coords = [0] * d

        if isinstance(d, (list, tuple)):
            self._coords = d

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

    def __neg__(self):
        """Returns the negative of a vector instance."""

        result = Vector(len(self))  # New vector to store negative vector.
        for j in range(len(self)):
            result[j] = -self[j]

        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """Return difference of two Vector instances.

        Performs u-v as -(-u+v)
        """
        negative = -self
        return -(negative.__add__(other))

    def __rsub__(self, other):
        """Computes v-u as -(u-v)."""
        return -(self.__sub__(other))

    def __eq__(self, other):
        """Return True if two Vector instances have same components."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if two Vector instances differ at some component."""
        return not (self == other)  # Relies on __eq__ defined above!

    def __str__(self):
        """Produces string representation of a Vector instance."""
        return '<' + str(self._coords)[1:-1] + '>'

    def __mul__(self, other):
        """Return either a scaled Vector instance, or the dot product of two Vector instances."""

        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for k in range(len(self)):
                result[k] = self[k] * other
            return result

        if len(self) != len(other):
            raise ValueError("Vectors must have same dimension.")

        result = 0
        for j in range(len(self)):
            result += self[j] * other[j]
        return result

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == "__main__":
    u = Vector(4)
    v = Vector([5, 6, -7, -1])

    u[0], u[1], u[2], u[3] = 1, 2, 3, 4
    # v[0], v[1], v[2], v[3] = 5, 6, -7, -1
    print(u)
    print(v)

    # w = u + v
    # print(w)
    #
    # print(u == v)
    # print(u is v)
    #
    # print(u * v)
    # print(v * u)
    #
    # print(u.scale(2.1))
    # print(u)
    #
    # # print(v.scale("hello"))
    #
    # print(-u)
    #
    # print(u+[-1,-2,-3,-4])
    # print([-1,-2,-3,-4]+u)

    print()
    print(u - [-1, -2, -3, -4])
    print([-1,-2,-3,-4] - u)

    print()
    print(u * 3)
    print(3 * u)

    print()
    print(u * v)
    print(v * u)