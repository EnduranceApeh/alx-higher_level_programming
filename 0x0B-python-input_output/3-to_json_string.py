#!/usr/bin/python3
"""
Module 3-to_json_string
This function retun a JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Return JSON representaion on an object"""

    json_str = json.dumps(my_obj)
    return json_str
