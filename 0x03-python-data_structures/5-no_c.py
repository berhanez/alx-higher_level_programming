#!/usr/bin/python3

def no_c(my_string):
    empty_str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            empty_str += i
    return (empty_str)
