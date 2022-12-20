#!/usr/bin/python3
"""Square class defined."""


class Square:
    """Square is created/represented."""
    def __init__(self, size=0):
        """new square initialized"""
        self.size = size

    @property
    def size(self):
        """ get current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Condition to ensure size is an integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """TO return area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defining for == condition of squares."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defining for != condition of squares."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defining for < condition of squares."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defining for <= condition of squares."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defining for > condition of squares."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defining for >= condition of squares."""
        return self.area() >= other.area()
