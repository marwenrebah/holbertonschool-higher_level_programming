#!/usr/bin/python3
"""add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        tab = load_from_json_file("add_item.json")
    except FileNotFoundError:
        tab = []
    tab.extend(sys.argv[1:])
    save_to_json_file(tab, "add_item.json")
