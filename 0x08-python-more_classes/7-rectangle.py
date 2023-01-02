#!/usr/bin/python3
""" Module defining the Rectangle class """


class Rectangle:
    """ Rectangle Class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializing a Rectangle
        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ int: width of the Rectangle. """
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
        """ int: height of the Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the Rectangle. """
        return self.height * self.width

    def perimeter(self):
        """ Returns the perimeter of the Rectangle. """
        return (self.height * 2) + (self.width * 2)
    def __str__(self):
        """  Return a string representation of Rectangle using '#' """
        if self.width is 0 or self.height is 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.width + '\n') *
                    (self.height - 1) + str(self.print_symbol) * self.width)

    def __repr__(self):
        """ Returns a string representation Rectangle that works with
            eval()"""
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    def __del__(self):
        """ Message when a Rectangle is deleted """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
