#!/usr/bin/python3
""" This module contains text indentation function. """


def text_indentation(text):
    """ Text indentation function

    Args:
        text (str): A string of text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c = c + 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c = c + 1
            while c < len(text) and text[c] == ' ':
                c = c + 1
            continue
        c = c + 1

