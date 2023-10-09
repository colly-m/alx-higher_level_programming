#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    max_val = my_list[0]

    for n in range(len(my_list)):
        if my_list[n] > max_val:
            max_val = my_list[n]

    return (max_val)
