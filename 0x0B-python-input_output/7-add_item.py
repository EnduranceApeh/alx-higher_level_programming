#!/usr/bin/python3
"""
A script that add all arguement to a python list
Save thislist to a file
"""
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Add all args to list
args_list = sys.argv[1:]
filename = "add_item.json"
my_list = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
