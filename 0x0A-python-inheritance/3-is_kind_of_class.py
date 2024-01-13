#!/usr/bin/python3
"""
Module 3-is_kind_of_class
This function return True if object is an instance a class
return flase otherwise
"""


def is_kind_of_class(obj, a_class):
    """Return true if object is instance of a class
    Return false otherwise
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
