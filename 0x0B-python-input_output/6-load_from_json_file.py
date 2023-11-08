#!/usr/bin/python3
"""Module to create an object from JSON file"""

import json


def load_from_json_file(filename):
    """loads an object from json into a file"""
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
