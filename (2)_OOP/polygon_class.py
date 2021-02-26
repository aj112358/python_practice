"""This module allows for the creation of various polygons, and computes their perimeter and area.

For now, we assume only *regular* polygons:
    - Triangle
    - Square
    - Pentagon
    - Hexagon
    - Octagon

Created By: AJ Singh
Date: Feb 25, 2021
"""

from math import sqrt
from abc import abstractmethod


class Polygon:
    """A class to create a general polygon, meant to specify the required methods for sub-classes."""

    def __init__(self, l):
        """Create a new regular polygon with side length l."""
        self._length = l

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Polygon):
    """Class to create a triangle."""

    def __init__(self, n):
        """Construct a new triangle."""
        super().__init__(n)

    def area(self):
        """Compute area of a triangle."""
        return sqrt(3) / 4 * self._length**2

    def perimeter(self):
        """Compute the perimeter of a triangle."""
        return 3 * self._length


if __name__ == "__main__":

    triangle = Triangle(2)
    print(triangle.area())
    print(triangle.perimeter())