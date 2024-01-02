#!/usr/bin/python3
"""
Module 2-square
Define class Square
"""


class Square:
    """
    class Square definition
    Args:
        size (int): size of a side in square

    """
    def __init__(self, size=0):
        """
        Initialize Square

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
        elif size < 0:
            raise ValueError("size must be >=0")
