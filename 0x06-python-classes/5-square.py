#!/usr/bin/python3
"""Square class defined."""


class Square:
    """Square is made."""
    def __init__(self, size=0):
        """Square is initialized."""
        self.size = size

    @property
    def size(self):
        """Set size of square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Tests if size is a positive integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Square made of #'s"""
        if self.__size is not 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
