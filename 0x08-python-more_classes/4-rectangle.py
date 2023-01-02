#!/usr/bin/python3
""" Defining a Rectangle class..."""


class Rectangle:
    """ Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): width of the rectangle.
            height (int)e height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width of the Rectangle."""
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
        """ height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return Rectangle Area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return Rectangle Perimeter."""
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Rectanglee using '#'char """
        if self.width is 0 or self.height is 0:
            return ""
        else:
            return (('#' * self.width + '\n') * (self.height - 1) +
                    '#' * self.width)

    def __repr__(self):
        """ Returns a str representation of Rectangle that works with
            eval() """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
