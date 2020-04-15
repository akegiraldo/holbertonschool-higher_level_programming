#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if (r.status_code == 200):
        print(r.text)
    else:
        print("Error code:", r.status_code)
