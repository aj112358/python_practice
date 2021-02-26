"""This module allows for the creation of various polygons, and computes their perimeter and area.

For now, we assume only *regular* polygons:
    - Triangle
    - Square
    - Pentagon
    - Hexagon
    - Octagon

TO-DO: For each shape, write down various ways to make it well-defined.

Created By: AJ Singh
Date: Feb 25, 2021
"""

from math import sqrt
from abc import abstractmethod


class Polygon:
    """A class to create a general polygon, meant to specify the required methods for sub-classes."""

    def __init__(self):
        """Create a new regular polygon with side length l."""
        # self._length = l

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Polygon):
    """Class to create a triangle."""

    def __init__(self, base, height):
        """Construct a new triangle."""
        super().__init__()
        self._base = base
        self._height = height

    def area(self):
        """Compute area of a triangle."""
        # return sqrt(3) / 4 * self._length**2
        return 0.5 * self._base * self._height

    def perimeter(self):
        """Compute the perimeter of a triangle."""
        return "hello"


if __name__ == "__main__":

    triangle = Triangle(3,5)
    print(triangle.area())
    print(triangle.perimeter())