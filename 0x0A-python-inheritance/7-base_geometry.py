#!/usr/bin/python3
""" Module contains the `BaseGeometry` class. """


class BaseGeometry:
    """ A BaseGeometry class. """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an integer and if it is > 0."""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
