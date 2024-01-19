#!/usr/bin/python3
"""
Module contain class base base

contain private class __nb_objects, and constructor __init__
"""
import json


class Base:
    """
    define class
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string rep of python dict"""
        if list_dictionaries is None:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str
