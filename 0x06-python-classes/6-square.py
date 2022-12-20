#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """ get or set position of square """
        return self.__position

    @position.setter
    def position(self, size):
        if (not isinstance(size, tuple) or
                len(size) != 2 or
                not all(isinstance(n, int) for n in size) or
                not all(n >= 0 for n in size)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = size

    def area(self):
        """ Return Area of Square """
        return self.__size ** 2

    def my_print(self):
        """ ### Square printer """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
