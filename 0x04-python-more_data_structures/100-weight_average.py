#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == {}:
        return (0)
    num = 0
    add = 0
    for i, j in my_list:
        num += i * j
        add += j
    return (num/add)
