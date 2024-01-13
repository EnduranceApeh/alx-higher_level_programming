#!/usr/bin/python3
"""
Module 2-is_same_class
return True is object is exactlyt an istance of class
return False otherwise
"""


def is_same_class(obj, a_class):
    """return if object is exaclty an instance of a class"""

    if type(obj) == a_class:
        return True
    else:
        return False
