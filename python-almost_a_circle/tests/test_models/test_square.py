#!/usr/bin/python3
import unittest
import pep8
from models.square import Square


class testcase(unittest.TestCase):
    """this is the class for unittest"""

    def test_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide()
        res = style.check_files(["models/square.py"])
        self.assertEqual(res.total_errors, 0, "pep8 error")

    def test_area(self):
        """check area"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)


if __name__ == "__main__":
    unittest.main()
