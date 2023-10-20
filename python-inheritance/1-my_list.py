#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
