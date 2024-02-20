#!/usr/bin/python3
"""Script to take in a aletter and send a POST request to a URL
The letter as the parameter"""
import requests
import sys


def search_alphabet(letter):
    """Module to fetch for a letter"""
    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}

    response = requests.post(url, data=params)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    search_alphabet(letter)
