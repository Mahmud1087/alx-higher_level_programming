#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    multiplies each values by 2
    """
    newDict = {}
    for i in a_dictionary:
        anotherDict = {i:a_dictionary[i]*2}
        newDict.update(anotherDict)
    return newDict
