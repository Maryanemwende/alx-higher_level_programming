#!/usr/bin/python3
"""
function that returns the dict desc with simple data structure
"""


def class_to_json(obj):
    """
     returns the dictionary description with simple data structure
     for JSON serialization of an object
     """
     return obj.__dict__
