#!/bin/usr/python3
def print_last_digit(number):
    if (number < 0):
        cp = (number * -1) % 10
    else:
        cp = number % 10
    print("{}".format(cp), end='')
    return cp
