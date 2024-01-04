#!/usr/bin/python3
"""
Module 4-square
Define class Square
"""


class Square:
    """
    class Square definition
    Args:
        size: size of square
    """
    def __init__(self, size=0):
        """
            Attribute:
                __size: A private attribute, if none the size is 0 by defualt

            Raises:
                TypeError: if size is not integer
                ValueError: if size is less than 0
        """
        self.__size = size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate the area of a square

        Return:
            int: The area of square
        """

        return self.__size ** 2
