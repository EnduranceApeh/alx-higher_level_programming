#!/usr/bin/python3
"""
Module 1-write_file
write string to text file and return num of character
"""


def write_file(filename="", text=""):
    """
    This function write a 
    string to a text and 
    return the number of character
    """

    with open(filename, 'w', encoding="utf-8") as rf:
       num = rf.write(text)
       return num
