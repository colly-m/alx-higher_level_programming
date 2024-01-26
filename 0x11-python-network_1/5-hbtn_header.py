#!/usr/bin/python3
"""Script to take a URL, send a request to it then displays the value
of variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    outcome = requests.get(url)
    print(outcome.headers.get('X-Request-Id'))
