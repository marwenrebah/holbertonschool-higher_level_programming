#!/usr/bin/python3
def no_c(my_string):
    my_string = ""
    for char in my_string:
        if char not in ('c', 'C'):
            my_string += char
    return my_string
