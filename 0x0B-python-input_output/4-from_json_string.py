#!/usr/bin/python3

"""The 4-from_json_string module"""

import json

def from_json_string(my_str):

    """to_json_string-def- to_json_string(my_obj)
    Args:
        my_str(str): the string
    Return:
         returns the JSON string representation
    """
    return json.loads(my_str)
