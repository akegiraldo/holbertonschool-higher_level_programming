#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    length = len(argv) - 1
    acu = 0
    if length == 0:
        print("0")
    else:
        for i in range(1, length + 1):
            acu += int(argv[i])
        print("{}".format(acu))
