#!/usr/bin/python3
import json
"""
Module 3-to_json_string
This function retun a JSON representation of an object
"""


def to_json_string(my_obj):
    """Return JSON representaion on an object"""

    json_str = json.dumps(my_obj)
    return json_str
