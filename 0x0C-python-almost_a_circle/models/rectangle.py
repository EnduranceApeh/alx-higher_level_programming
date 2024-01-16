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
    definning class Rectangle which inherit from Basei
    Inherited attribute:
        id

    class Attributes:
        __width     __height
        __y         __x

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
        return self.__width

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

    def area(self):
        """Returns the area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle instance with the character #"""
        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return string representation of object"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign *args to attributes"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.width = kwargs['width']
            if "heigth" in kwargs:
                self.height = kwargs['height']
            if "x" in kwargs:
                self.x = kwargs['x']
            if "y" in kwargs:
                self.y = kwargs['y']
