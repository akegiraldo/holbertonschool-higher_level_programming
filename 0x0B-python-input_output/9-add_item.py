#!/usr/bin/python3
from sys import argv
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    ls = load_from_json_file("add_item.json")
except:
        ls = []

for i in range(1, len(argv)):
    ls.append(argv[i])

save_to_json_file(ls, "add_item.json")
