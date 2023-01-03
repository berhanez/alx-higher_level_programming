#!/usr/bin/python3
""" Module that defines a locked class."""


class LockedClass:
    """ Prevent the user from implementing new Locked Class attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
