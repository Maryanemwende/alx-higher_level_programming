#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    for idx in set(my_list):
        addition += idx
    return addition
