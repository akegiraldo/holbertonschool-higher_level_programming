#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge:
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”.
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/"+repo+"/"+owner+"/commits"
    try:
        r = requests.get(url).json()
        i = 0

        while (i < 10):
            print(r[i]['sha']+": "+r[i]['commit']['author']['name'])
            i += 1
    except:
        pass
