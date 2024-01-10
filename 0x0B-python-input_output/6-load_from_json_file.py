#!/usr/bin/python3
"""
Module 6-load_from_json_file
This function create an object from JSON file
"""
import json


def load_from_json_file(filename):
    """Create an object from JSON file"""

    with open(filename, encoding="utf-8") as file:
        my_obj = json.load(file)
        return my_obj
