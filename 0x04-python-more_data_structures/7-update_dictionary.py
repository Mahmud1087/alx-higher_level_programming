#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    b_dict = {key:value}
    a_dictionary.update(b_dict)
    return a_dictionary
