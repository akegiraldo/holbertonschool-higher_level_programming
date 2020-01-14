#!/usr/bin/python3
"""Module to find the max integer"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    may = list[0]
    i = 1
    while i < len(list):
        if list[i] > may:
            may = list[i]
        i += 1
return may
