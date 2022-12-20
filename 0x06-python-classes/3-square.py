#!/usr/bin/python3
"""Square class defined."""


class Square:
    """Square is made."""
    def __init__(self, size=0):
        """Square is initialized."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square."""
        return (self.__size ** 2)
