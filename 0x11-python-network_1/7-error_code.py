#!/usr/bin/python3
"""Script to take a URL, send a request to it and display the response body"""
import requests
import sys


if __name__ == "__main__":
    """Check for the correct number of command-line arguments"""
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)

    """Check the HTTP status code"""
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
