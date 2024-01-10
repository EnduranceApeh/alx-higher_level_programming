#!/usr/bin/python3
"""
Module 1-write_file
write string to text file and return num of character
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as rf:
        return rf.write(text)
