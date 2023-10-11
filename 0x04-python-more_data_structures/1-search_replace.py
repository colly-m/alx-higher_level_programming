#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for obj in my_list:
        if obj == search:
            n_list.append(replace)
        else:
            n_list.append(obj)

    return (n_list)
