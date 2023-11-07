#!/usr/bin/python3
"""Module to write an object into a text file using JSON"""

import json


def save_to_json_file(my_obj, filename):
    """using with to access the file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file,ensure_ascii=False)
