#!/usr/bin/python3
"""
Module 1-write_file
This function read text and print to stdout
"""


def read_file(filename=""):
    """read text and print to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
