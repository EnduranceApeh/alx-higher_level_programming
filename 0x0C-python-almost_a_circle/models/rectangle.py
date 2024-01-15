#!/usr/bin/python3
"""
module conatin class Base
This class inherit from class Base
contain private instance attribue
each with its own getter and setter
"""
from models.base import Base


class Rectangle(Base):
    """
    definning class Rectangle which inherit from Base

    Methods:
        __init__(self, width, hheight, x=0, y=0, id=None)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return  self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def y(self):
        """y getter"""
        return self.__y

    @property
    def x(self):
        """x getter"""
        return self.__x

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
