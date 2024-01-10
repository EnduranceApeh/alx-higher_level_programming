#!/usr/bin/python3
"""
Module 1-write_file
This function read text and print to stdout
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
        f.close()
