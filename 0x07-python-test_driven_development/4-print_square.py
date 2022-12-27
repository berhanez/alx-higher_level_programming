#!/usr/bin/python3
""" This module contains function that prints a square with #. """


def print_square(size):
    """ Function that prints a square using '#' based on `size` parameter."""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
