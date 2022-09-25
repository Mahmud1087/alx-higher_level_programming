#!/usr/bin/python3
def no_c(my_string):
    newItem = my_string.translate({ord(c): None for c in "cC"})
    return newItem
