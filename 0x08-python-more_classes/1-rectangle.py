#!/usr/bin/python3
""""
Module 1-rectangle
Define class Rectangle
"""


class Rectangle:
    """
    class Rectangle definition
    Args:
        width: width of rectangle
        height: height of rectangle
    """

    def __init__(self, width=0, height=0):
        """"
        Attributes:
            __width (int): private attribute that store the width of rectangle
            __height (int): private attribute for rectangle height
        Raises:
            TyperError: if width and height is not int type
            ValueError: if width and height is < 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter

        Return:width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value: set width to value if > 0
        """
        if type(self.width) != int:
            raise TypeError("width must be an integer")
        elif self.width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter

        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value: set height to value if >= 0
        """

        if type(self.height) != int:
            raise TypeError("height must be an integer")
        elif self.height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
