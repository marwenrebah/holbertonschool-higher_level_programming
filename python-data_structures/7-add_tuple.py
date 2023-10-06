#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    if la < 2:
        for i in range(2 - la):
            tuple_a += (0,)
    if lb < 2:
        for i in range(2 - lb):
            tuple_b += (0,)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    return (a, b)
