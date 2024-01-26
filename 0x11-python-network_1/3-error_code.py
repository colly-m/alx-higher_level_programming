#!/usr/bin/python3
"""Script to take a URL, send a request to it and display the body response"""
import sys
import urllib.parse
import urllib.request


def fetch_url_body(url):
    """Module to fetch the contents"""
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_body(url)
