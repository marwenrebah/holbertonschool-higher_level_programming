#!/usr/bin/python3
"""list class MyList."""


class MyList(list):
    """My list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))