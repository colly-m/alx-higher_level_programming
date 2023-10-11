#!/usr/bin/python3
def uniq_add(my_list=[]):
    unq_ints = set()
    result = 0

    for n in my_list:
        if n not in unq_ints:
            result += n
            unq_ints.add(n)

    return (result)
