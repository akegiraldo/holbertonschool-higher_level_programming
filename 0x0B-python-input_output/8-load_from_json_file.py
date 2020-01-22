#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, encoding="UTF-8") as a:
        txt = a.read()
        return json.loads(txt)
