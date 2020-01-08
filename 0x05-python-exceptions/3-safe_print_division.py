#!/usr/bin/python3


def safe_print_division(a, b):
    t = 0
    c = 0
    try:
        c = a / b
        print("Inside result: {}".format(c))
    except ZeroDivisionError:
        print("Inside result: None")
        t = 1
    finally:
        if t == 0:
            return uc
        else:
            return None
