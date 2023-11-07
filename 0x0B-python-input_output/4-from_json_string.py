#!/usr/bin/python3
"""Function to return  an object from_json_string module """

import json


def from_json_string(my_str):
    """Return a JSON object """
    return json.loads(my_str)
