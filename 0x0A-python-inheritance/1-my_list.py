#!/usr/bin/python3
"""
Module 1-my_list
A class that inherit from list
print sorted list
"""


class MyList(list):
    """
    Inherit from list

    method:
        print_sorted (self)
    """

    def print_sorted(self):
        print(sorted(self))
