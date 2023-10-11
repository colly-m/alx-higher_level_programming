#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    skeys = sorted(a_dictionary.keys())

    for key in skeys:
        val = a_dictionary[key]
        print(f"{key}: {val}")
