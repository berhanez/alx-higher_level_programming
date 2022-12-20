#!/usr/bin/python3
"""Square class defined"""


class Square:
    """Square is made."""
    def __init__(self, size=0):
        """Square is initialized."""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
