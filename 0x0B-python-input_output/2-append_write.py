#!/usr/bin/python3
"""Function to append a string at end of a text file"""


def append_write(filename="", text=""):
    """Count the number of characters to be added"""
    char_count = len(text)

    """Use the with statement to automatically close the file after writing"""
    with open(filename, 'a', encoding='utf8') as file:
        """Write the text at the end of the file"""
        file.write(text)
        return (char_count)
