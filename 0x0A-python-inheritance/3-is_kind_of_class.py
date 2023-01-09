#!/usr/bin/python3
""" Module containing the `is_kind_of_class` function. """


def is_kind_of_class(obj, a_class):
    """ Check if `obj` is an instance of a `a_class` or a child class
    Returns: True if `obj` is an instance a `a_class`, otherwise False.
    """
    return isinstance(obj, a_class)
