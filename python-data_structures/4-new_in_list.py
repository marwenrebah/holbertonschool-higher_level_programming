#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = my_list[:]
    if idx >= 0 and idx < len(x):
        x[idx] = element
    return x
