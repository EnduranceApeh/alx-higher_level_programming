#!/usr/bin/python3
"""
Module 100-my_int.py

contain a class MyInt that inherit from Int(BaseClass)
"""


class MyInt(int):
    """
    Methods:
        __init__(self, num)
        __eq__(self, other)
        __ne__(self, other)
    """
    def __init__(self, num):
        """initialize num"""
        self.num = num

    def __eq__(self, other):
        """
        Return:
           True if both not equal
        """
        return self.num != other

    def __ne__(self, other):
        """
        Return:
           True if both equal
        """
        return self.num == other
