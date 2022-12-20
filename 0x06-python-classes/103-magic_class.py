#!/usr/bin/python3
"""Pycode that mimics exactly what the bytecode does."""
import math


class MagicClass:
    """Circle representation."""

    def __init__(self, radius=0):
        """The initialization of circle parameters."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("THE RADIUS MUST BE A DIGIT")
        self.__radius = radius

    def area(self):
        """GET AREA of cicle equivalent to = (pi)(r)(r)."""
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """GET Circumference of circle defined as  = 2(pi)(r)"""
        return (2 * math.pi * self.__radius)
