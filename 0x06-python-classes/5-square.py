"""
Module 5-square
Define class Square
"""


class Square:
    """
    Initialize size
    Attribut:
        __size (int): private attribute of typr int
    """
    def __init__(self, size):
        """
        Args:
            size: size of side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter

        Return: size of sqaure
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: set size to value if int and >= 0"
        """
        self.__size = value
        if type(self.size) != int:
            raise TypeError("size must be an integer")
        elif self.size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__square)**2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            self.j = 0
            while self.j < self.size:
                for i in range(self.size):
                        print("#", end="")
                self.j += 1
             print()
