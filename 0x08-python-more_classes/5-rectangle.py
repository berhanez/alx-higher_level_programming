#!/usr/bin/python3
""" Module defininf a Rectangle class. """


class Rectangle:
    """ Representing a Rectangle Class. """

    def __init__(self, width=0, height=0):
        """ Initializing an instance of ``Rectangle``
        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width of the Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of the Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area. """
        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter. """
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """Rectangle using '#' char """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (('#' * self.width + '\n') * (self.height - 1) +
                    '#' * self.width)

    def __repr__(self):
        """ Returns a str representation of Rectangle[eval()] """
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    def __del__(self):
        """ Prints a message for when rectangle  is deleted. """
        print("Bye rectangle...")
