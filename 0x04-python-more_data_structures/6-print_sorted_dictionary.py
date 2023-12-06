#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # print dictionary by ordered key
    for key, value in sorted(a_dictionary.items()):
        print("{:s}: {}".format(key, value))
