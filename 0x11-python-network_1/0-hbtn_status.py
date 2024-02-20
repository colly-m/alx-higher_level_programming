#!/usr/bin/python3
"""Script to fetch https://alx-intranet.btn.io/status"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read()
    decoded_html = html.decode('utf-8')
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(decoded_html))
