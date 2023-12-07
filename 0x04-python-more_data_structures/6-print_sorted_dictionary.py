#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    # print dictionary by ordered key
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
