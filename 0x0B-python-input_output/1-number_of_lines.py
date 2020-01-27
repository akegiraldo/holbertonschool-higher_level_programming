#!/usr/bin/python3


def number_of_lines(filename=""):
    i = 0
    with open(filename, encoding='UTF8') as a:
        for line in a:
            i += 1
    return i
