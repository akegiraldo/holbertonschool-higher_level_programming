#!/usr/bin/python3
"""
Script that takes your Github credentials (username and password) and
uses the Github API to display your id.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    pwd = argv[2]

    try:
        r = requests.get(url, auth=(user, pwd)).json()
        print(r["id"])
    except:
        print("None")
