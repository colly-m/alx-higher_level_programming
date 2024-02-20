#!/usr/bin/python3
"""Script to take in a URL, sends a request to it and displays value of
X- Request-Id variable found in the header"""
import urllib.request
import sys


if __name__ == "__main__":
    """Check if a URL is provided as a command-line argument"""
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get('X-Request-id'))
