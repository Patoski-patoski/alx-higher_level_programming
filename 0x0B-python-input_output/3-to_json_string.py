#!/usr/bin/python3


"""The 3-to_json_string module"""

import json

def to_json_string(my_obj):

    """to_json_string-def- to_json_string(my_obj)
    Args:
        obj (str): the object
    Return:
         returns the JSON string representation
    """
    return json.dumps(my_obj)
