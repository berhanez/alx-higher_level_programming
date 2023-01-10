#!/usr/bin/python3
""" defining a .txt file reader function. """

def read_file(filename=""):
    """Print the contents of text file(UTF-8) to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
