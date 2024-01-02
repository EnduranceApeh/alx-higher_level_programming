#!/usr/bin/python3
"""
Module 2-square
Define class Square
"""


class Square:
    """class Square definition"""
    def __init__(self, size=0):
        """
        Attributes:
            size: size of square
        Raise:
            TypeError: if size is not an int value.
            ValueError: if size is less than 0.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
