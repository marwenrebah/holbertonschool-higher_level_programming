#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json


def save_to_json_file(my_obj, filename):
    """Save object to a JSON file."""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Load object from a JSON file."""
    with open(filename, mode="r") as f:
        return json.load(f)


if __name__ == "__main":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
