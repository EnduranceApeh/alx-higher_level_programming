#!/usr/bin/python3
"""
Module 4-inherits_from
This function return True is an instance of a 
    class inherited from a specified class
return False otherwise
"""


def inherits_from(obj, a_class):
    """
    Return true if the object in instance of a class
    that inherited from a specified class otherwise False
    """

    if isinstance(a_class, obj):
        return True
    else:
        return False
