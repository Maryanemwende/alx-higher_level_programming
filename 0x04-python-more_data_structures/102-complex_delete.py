#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for ky, vl in a_dictionary.items():
            if vl == value:
                del a_dictionary[ky]
                break
    return a_dictionary
