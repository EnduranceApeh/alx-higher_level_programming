#!/usr/bin/python3
"""
Module 5-save_to_json_file
This function write an object to text file, using:
    JSOn representaion
"""
import json


def save_to_json_file(my_obj, filename):
    """write an objectt txt file using JSON"""

    with open(filename, 'w', encoding="utf-8") as json_repr:
        json.dump(my_obj, json_repr)
