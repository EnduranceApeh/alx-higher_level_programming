#!/usr/bin/python3
"""
A script that add all arguement to a python list
Save thislist to a file
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Add all args to a list
args_list = sys.argv[1:]
my_list = save_to_json_file(args_list, "add_item.json")
load_from_json_file("add_item.json")
