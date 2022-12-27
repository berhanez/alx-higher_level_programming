#!/usr/bin/python3
""" Module containing add_integer function that adds two ints. """


def add_integer(a, b=98):
    """ Sum up two integers and return result. """
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return (a + b)
