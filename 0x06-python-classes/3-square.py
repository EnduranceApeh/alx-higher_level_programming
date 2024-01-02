#!/usr/bin/python3
"""
Module 3-square
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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate the area of a square

        Return:
            int: The area of square
        """

        return self.__size ** 2
