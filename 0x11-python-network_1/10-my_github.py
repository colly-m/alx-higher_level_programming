#!/usr/bin/python3
"""Script to take github credentials and uses its API to display id
"""
import sys
from requests import get, auth


if __name__ == "__main__":
    url = 'https://api.github.com/username'
    username = sys.argv[1]
    password = sys.argv[2]
    request = get(url, auth=auth.HTTPBasicAuth(username, password))
    print(request.json().get('id'))
