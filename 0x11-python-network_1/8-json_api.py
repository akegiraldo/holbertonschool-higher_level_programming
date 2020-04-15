#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        value = ""
    else:
        value = argv[1]
    r = requests.post(url, data={'q': value})
    try:
        json = r.json()
        if len(json) == 2:
            print("[{}] {}".format(json['id'], json['name']))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
