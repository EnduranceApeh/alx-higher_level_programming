#!/usr/bin/python3
"""
Module 0-lookup
This function return list of available atrribute and method of obj
"""


def lookup(obj):
    """Returns list of available attribute anf method of obj"""

    method_attr = print(dir(obj))
    return method_attr
