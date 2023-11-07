#!/usr/bin/python3
"""Module to write a string into a file returning characters count"""


def write_file(filename="", text=""):
    """Defines function to insert text into a file"""
    if filename == "" or text == "":
        return "Invalid input. Filename and text are required."
    with open(filename, 'w', encoding='utf8') as file:
        file.write(text)
    return len(text)
