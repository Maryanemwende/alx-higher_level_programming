#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    rval = list(a_dictionary.keys())[0]
    max_int = a_dictionary[rval]
    for ky, vl in a_dictionary.items():
        if vl > max_int:
            max_int = vl
            rval = ky
    return rval
