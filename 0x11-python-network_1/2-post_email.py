#!/usr/bin/python3
"""Script to take a URL and an email, send a POSt request to it with email"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """Check if both URL and email are provided as arguments"""
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    param = urllib.parse.urlencode(data).encode("ascii")

    request = urllib.request.Request(url, param)
    with urllib.request.urlopen(request) as response:
        outcome = response.read().decode('utf-8')
        print(outcome)
