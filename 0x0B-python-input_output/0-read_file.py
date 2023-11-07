#!/usr/bin/python3
"""Module function to read a text file UTF* ansd prints it"""


def read_file(filename=""):
    """defines module to read into a file"""
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            print(line, end='')
