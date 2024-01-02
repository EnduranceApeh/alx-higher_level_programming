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
        """
        self.__size = size
        """
        Raise:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
