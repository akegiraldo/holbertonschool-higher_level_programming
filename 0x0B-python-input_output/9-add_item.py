#!/usr/bin/python3
import json
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    list_to_json = load_from_json_file("add_item.json")
except:
        list_to_json = []

for i in range(1, len(argv)):
    list_to_json.append(argv[i])

save_to_json_file(list_to_json, "add_item.json")
