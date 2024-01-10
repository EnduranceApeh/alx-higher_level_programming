#!/usr/bin/python3
"""
Module 4-from_json_string
This function return an object (Python data struc)
represented by JSON string
"""
import json


def from_json_string(my_str):
    """Return an object represented by JSON string"""

    json_obj = json.loads(my_str)
    return json_obj
