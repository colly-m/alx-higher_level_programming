#!/usr/bin/python3
"""Script to take github credentials and uses its API to display id
"""
import requests
import sys


username = sys.argv[1]
password = sys.argv[2]


auth_header = requests.auth.HTTPBasicAuth(username, password)

""" Make a GET request to the GitHub API to retrieve the user information"""
response = requests.get("https://api.github.com/user", auth=auth_header)

if response.status_code == 200:

    user_id = response.json()["id"]
    print(f"{user_id}")
else:
    print("None")
