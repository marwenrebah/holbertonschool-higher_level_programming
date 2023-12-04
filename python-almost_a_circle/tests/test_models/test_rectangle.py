#!/usr/bin/python3
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base


class testcase(unittest.TestCase):
    """this is the class for unittest"""

    def test_pep8(self):
        """pep8 test"""
        style = pep8.StyleGuide()
        res = style.check_files(["models/rectangle.py"])
        self.assertEqual(res.total_errors, 0, "pep8 error")

    def test_val(self):
        """test values"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

    def test_positive(self):
        """test if the value isn't positive"""
        self.assertRaises(ValueError, Rectangle, -10, -2, 0, 0, -12)

    def test_string(self):
        """test if type is string"""
        self.assertRaises(
            TypeError, Rectangle, "hello", "io", "Xz", "89", "-12")

    def test_float(self):
        """test if type is float"""
        self.assertRaises(TypeError, Rectangle, 1.1, 32.66, 88.963,
                          0.25, 7.0)

    def test_bool(self):
        """test if type is boolean"""
        self.assertRaises(
            ValueError, Rectangle, True, False, True, False, True)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_str_method(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
