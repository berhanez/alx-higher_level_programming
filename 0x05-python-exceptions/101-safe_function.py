#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as err:
        return None
    else:
        return result
