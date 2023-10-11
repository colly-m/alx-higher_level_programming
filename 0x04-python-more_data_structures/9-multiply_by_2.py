#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    resDictionary = {}

    for key, value in a_dictionary.items():
        resDictionary[key] = value * 2

    return (resDictionary)
