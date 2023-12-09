#!/usr/bin/python3

""" script that adds all arguments to a Python list, and then save them
to a file

Usage:
        add_item arg1 arg2 ...

        If the file doesn’t exist, create
        load_from_json_file: loads the file for deserializing
        command line args are made into list
        load_from_json_file: list are saved back into the file
        by serializing them
"""
from sys import argv
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_obj = []

# Append command line arguments to my_obj
for arg in argv[1:]:
    my_obj.append(arg)

# Load existing data from file
loaded = load_from_json_file('add_item.json')

# Append new data to the loaded list
for arg in my_obj:
    loaded.append(arg)

# Save the updated list to the file
save_to_json_file(loaded, 'add_item.json')
