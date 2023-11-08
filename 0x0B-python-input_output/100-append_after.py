#!/usr/bin/python3
"""Function to insert text into a fle after each line with specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Class body"""
    txt = ""
    with open(filename) as fil:
        for line in fil:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
