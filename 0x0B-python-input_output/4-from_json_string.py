#!/usr/bin/python3
"""define a json-to-obj function"""


import json


def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    """
    return json.loads(my_str)

