#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary is False:
        return a_dictionary
    else:
        del a_dictionary[key]
