"""A library for various number sequences, taken from book.

Created By: AJ Singh
Date: Feb 13, 2021
"""

from math import sqrt


class Progression:
    """An iterator class to produce a generic progression.

    The default is simple 0,1,2,...
    This is meant to be inherited from to produce your own numeric progression.
    """

    def __init__(self, start=0):
        """Initialize 'current' instance variable to first value of progression."""

        self._current = start

    def _advance(self):
        """Update 'current' instance variable to the new value.

        This method is meant to be overridden by a subclass to create you own definition of how to generate the next
        term in the sequence you are making.

        By convention, is 'current' is set to None -> this designates the end of a finite progression.
        """

        self._current += 1

    def __next__(self):
        """Return the next element int the progression, or raise StopIteration exception."""

        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current  # Current value to return.
            self._advance()  # Generate the next value (i.e. just getting it ready).
            return answer  # Return current value (i.e. to the user, this will be the *next* value.

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print the NEXT n values of the progression"""
        print(" ".join(str(next(self)) for _ in range(n)))


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        @param increment:   fixed constant to add to each term (default 1)
        @param start:       first term of the progression (default 0
        """

        super().__init__(start)  # Need to initialize the base class.
        self._increment = increment  # Remaining initialization for this class.

    # Override inherited version, so as to define our own progression formula.
    def _advance(self):
        """Update current value by adding the fixed increment value."""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator for producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Creates a new geometric progression.

        @param base:    fixed constant multiplier (aka: "common ratio") (default 2)
        @param start:   starting value (default 1)
        """

        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying the common ratio."""
        self._current *= self._base


class FibonacciProgression(Progression):
    """An iterator to produce a Fibonacci-type sequence.

    Uses two values as initializations. Produces next term by adding the two previous values.
    """

    def __init__(self, first=0, second=1):
        """Creates a new Fibonacci-type sequence.

        @param first:   first value (default 0)
        @param second:  second value (default 1)
        """

        super().__init__(first)  # Initializes _current to 'first'.
        self._second = second

    def _advance(self):
        """Rule for generating next term in the sequence."""

        self._current, self._second = self._second, self._current + self._second


class AbsoluteDifferenceProgression(Progression):
    """Generates a sequence where the terms are the absolute value of difference of previous two values."""

    def __init__(self, first=2, second=200):
        """Construct a new sequence."""

        super().__init__(first)
        self._second = second

    def _advance(self):
        """Rule for generating the next term in the sequence."""
        self._current, self._second = self._second, abs(self._current - self._second)


class SquareRootProgression(Progression):
    """Generates a sequence of square root values."""

    def __init__(self, first=65536):
        """Construct a new sequence generator."""
        super().__init__(first)

    def _advance(self):
        """Compute next term in the sequence."""
        self._current = round(sqrt(self._current), 4)


if __name__ == "__main__":
    seq = Progression()
    seq.print_progression(5)
    next(seq)
    print(next(seq))
    seq.print_progression(5)

    print("*" * 10)

    arithmetic = ArithmeticProgression(start=0, increment=5)
    arithmetic.print_progression(10)
    next(arithmetic)
    arithmetic.print_progression(2)

    print("*" * 10)

    geometric = GeometricProgression(start=3, base=3)
    geometric.print_progression(6)

    print("*" * 10)

    fibonacci = FibonacciProgression(first=0, second=1)
    fibonacci.print_progression(10)

    fibonacci = FibonacciProgression(first=2, second=2)
    fibonacci.print_progression(8)

    print("*" * 10)

    abs_diff = AbsoluteDifferenceProgression()
    abs_diff.print_progression(10)

    print("*" * 10)

    sqr_root_seq = SquareRootProgression(first = 1024)
    sqr_root_seq.print_progression(10)