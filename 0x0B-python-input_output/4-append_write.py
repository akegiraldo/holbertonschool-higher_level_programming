#!/usr/bin/python3


def append_write(filename="", text=""):
    w = 0
    with open(filename, 'a', encoding='UTF8') as a:
        w = a.write(text)
    return w
