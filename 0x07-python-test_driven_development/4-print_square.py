#!/usr/bin/python3
"""
Module 4-print_square
This function print a square with character #
"""


def print_square(size):
    """print square with character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print()
