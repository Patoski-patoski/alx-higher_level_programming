#!/usr/bin/python3

""" Test for rectangle module"""

import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test for Rectangle class"""

    def setUp(self):
        """To be called before the start of any test function"""
        Base._Base__nb_objects = 0

    def test_attributes(self):
        """Test to check if attributes are correctly set"""

        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_assignment(self):
        """Test to check if id is assigned correctly"""
        r1 = Rectangle(100, 4)
        r2 = Rectangle(200, 21, 2)
        self.assertEqual(r1.width, 100)
        self.assertEqual(r2.x, 2)

    def test_type(self):
        """Test to check if id is of type int"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r1.x, int)

    def test_setters(self):
        """Test for setters and getters"""
        r1 = Rectangle(100, 200, 300, 400, 500)
        r1.width = 1
        r1.height = 2
        r1.x = 3
        r1.y = 4
        r1.id = 5
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_errors(self):
        """Test for type and value errors for setters and getters"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "invalid", 7, -10, 9)
        r2 = Rectangle(1, 3, 7, 10, 9)
        with self.assertRaises(ValueError):
            r2.y = -8
        with self.assertRaises(TypeError):
            r2.width = "Christ is Lord"

    def test_area(self):
        """Test for area of Rectangle"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test to display hash(#)"""
        r1 = Rectangle(1, 2)
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        r1.display()
        sys.stdout = sys.__stdout__
        expected_output = "#\n#\n"
        self.assertEqual(capturedoutput.getvalue(), expected_output)

    def test_str(self):
        """Test to override __str__"""
        r = Rectangle(3, 2, 1, 4, 5)
        expected_output = "[Rectangle] (5) 1/4 - 3/2"
        self.assertEqual(str(r), expected_output)

    def test_var_args(self):
        """Test for variable numbers of positional arguments (*args)"""
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_kwargs(self):
        """Test for variable numbers of non-positional arguments (**kwargs)"""
        r2 = Rectangle(10, 10, 10, 10, 1)

        r2.update(height=1)
        self.assertEqual(str(r2), "[Rectangle] (1) 10/10 - 10/1")

        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/3 - 4/2")

    def test_dictionary(self):
        """Test to return dictionary"""
        r9 = Rectangle(10, 2, 1, 9)
        r9_dict = r9.to_dictionary()
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r9_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
