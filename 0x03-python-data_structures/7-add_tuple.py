#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    v_a1, v_a2, v_b1, v_b2 = 0, 0, 0, 0
    if (len(tuple_a) == 0):
        v_a1 = 0
        v_a2 = 0
    elif (len(tuple_a) == 1):
        v_a1 = tuple_a[0]
        v_a2 = 0
    else:
        v_a1 = tuple_a[0]
        v_a2 = tuple_a[1]
    if (len(tuple_b) == 0):
        v_b1 = 0
        v_b2 = 0
    elif (len(tuple_b) == 1):
        v_b1 = tuple_b[0]
        v_b2 = 0
    else:
        v_b1 = tuple_b[0]
        v_b2 = tuple_b[1]
    tuple_c = (v_a1 + v_b1, v_a2 + v_b2)
    return tuple_c
