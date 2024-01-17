#!/usr/bin/python3
"""
Module square
contain class Square that inherit from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining class Square that inherit from Rectangle
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        __str__(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square instance

        Args:
            size(int): size of Square
            x(int): y of square
            x(int): x of square
            id(int): identification number of square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width
    @size.setter
    def size(self, value):
        """setter for size, set value of wodth and height to size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)
