#!/usr/bin/python3
import math

class MagicClass:

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("THE RADIUS MUST BE A DIGIT")
        self.__radius = radius
