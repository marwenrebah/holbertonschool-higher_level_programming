#!/usr/bin/python3
import unittest
import pep8
from models.base import Base


class test(unittest.TestCase):
    """this is the class for unittest"""

    def test_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide()
        res = style.check_files(["models/base.py"])
        self.assertEqual(res.total_errors, 0, "pep8 error")


if __name__ == "__main__":
    unittest.main()
