#!/usr/bin/python3
""""
Module 0-add_integer
This method return a int sum
Recieves two args int or float data type,typecast float to int before returning sum
"""


def add_integer(a, b=98):
    """Returns a + b as int"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
