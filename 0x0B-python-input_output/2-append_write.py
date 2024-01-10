#!/usr/bin/python3
"""
Module 2-append_write
write string to text file and return num of character
"""


def append_write(filename="", text=""):
    """
    This function append a str to the end of a text file and return the number of character
    """

    with open(filename, 'a', encoding="utf-8") as af:
        num_charac = af.write(text)
        return num_charac
