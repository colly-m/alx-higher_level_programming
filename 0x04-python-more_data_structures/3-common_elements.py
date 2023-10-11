#!/usr/bin/python3
def common_elements(set_1, set_2):
    cmnSet = set()

    for elm in set_1:
        if elm in set_2:
            cmnSet.add(elm)

    return (cmnSet)
