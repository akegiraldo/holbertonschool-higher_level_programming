#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge:
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”.
"""

import base64
import requests
from sys import argv

if __name__ == "__main__":
    client_key = argv[1]
    client_secret = argv[2]
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
