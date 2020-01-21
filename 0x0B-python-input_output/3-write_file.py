#!/usr/bin/python3


def write_file(filename="", text=""):
    w = 0
    with open(filename, 'w', encoding='UTF8') as a:
        w = a.write(text)
    return w
