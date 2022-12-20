#!/usr/bin/python3
import math


class MagicClass:

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("THE RADIUS MUST BE A DIGIT")
        self.__radius = radius

    """GET AREA = (pi)(r)(r)"""
    def area(self):
        return (math.pi * self.__radius ** 2)

    """GET Circumference = 2(pi)(r)"""
    def circumference(self):
        return (2 * math.pi * self.__radius)
