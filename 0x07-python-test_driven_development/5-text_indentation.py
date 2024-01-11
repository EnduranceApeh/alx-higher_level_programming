#!/usr/bin/pthon3
"""
Module 5-text_indentation.py
This function iterate over a string
print new line when specail character(?, : and .) is encountered
"""


def text_indentation(text):
    """Print new line when (?, : and .) is encountered"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
    print()
