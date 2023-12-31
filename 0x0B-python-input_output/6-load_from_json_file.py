#!/usr/bin/python3
"""
6-load_from_json_file module
load_from_json_file function
"""
import json
import os


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”

    Args:
        filename: serialized file to load from

    Return:
        a deserialized output
    """
    with open(filename, 'r', encoding='utf-8') as f:
        if os.path.exists(filename):
            return (json.load(f))
        return []
