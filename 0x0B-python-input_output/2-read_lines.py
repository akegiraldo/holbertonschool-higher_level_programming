#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    i = 0
    with open(filename, encoding='UTF8') as a:
        for line in a:
            i += 1
            if (nb_lines <= 0 or i <= nb_lines):
                print(line, end='')
