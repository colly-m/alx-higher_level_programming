#!/usr/bin/python3
"""Script to take a URL and email address, send a POST request passed to it
with email as parameter displaying the response body
"""
import requests
import sys


def send_post_request(url, email):
    """Module to get the response"""
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    print(response_body)
