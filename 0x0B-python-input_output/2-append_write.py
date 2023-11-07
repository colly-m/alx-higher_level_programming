#!/usr/bin/python3
"""Function to append a string at end of a text file"""



def append_write(filename="", text=""):
    """Use the with statement to automatically close the file after writing"""
    with open(filename, 'a', encoding='utf-8') as file:
        return (my_file.write(text))
