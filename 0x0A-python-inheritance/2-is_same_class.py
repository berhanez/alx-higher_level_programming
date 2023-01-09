#!/usr/bin/python3
""" Module contains`is_same_class` function. """


def is_same_class(obj, a_class):
    """Check if `obj` is an exact instance of `a_class`."""
    return (type(obj) is a_class)
