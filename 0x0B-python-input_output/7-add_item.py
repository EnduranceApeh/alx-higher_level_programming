#!/usr/bin/python3
"""
A script that add all arguement to a python list
Save thislist to a file
"""
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args_list = sys.argv[1:]
filename = "add_item.json"
my_list = load_from_json_file(filename)
combined_list = my_list + args_list
save_to_json_file(combined_list, filename)
