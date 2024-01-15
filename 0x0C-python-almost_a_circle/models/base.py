#!/usr/bin/python3
"""
Module contain class base base

contain private class __nb_objects, and constructor __init__
"""


class Base:
    """
    define class
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialiazing id
        Args:
                id (int): keep track of object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
