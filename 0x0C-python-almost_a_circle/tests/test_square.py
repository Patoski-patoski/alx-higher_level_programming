#!/usr/bin/python3

"""The test_square module"""

import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """the TestSquare class"""

    def setUp(self):
        """Setting Up definitions"""
        self.s4 = Square(5, 4, 3, 2)
        Base_nb__objects = 0

    def test_initialization(self):
        """Test initialization of Square"""

        self.assertEqual(self.s4.width, 5)
        self.assertEqual(self.s4.height, 5)
        self.assertEqual(self.s4.x, 4)
        self.assertEqual(self.s4.y, 3)
        self.assertEqual(self.s4.id, 2)

    def test_str_representation(self):
        """Test string representation of square"""

        expected_str = "[Square] (2) 4/3 - 5"
        self.assertEqual(str(self.s4), expected_str)

    def test_inheritance_from_rect(self):
        """Test inheritance of attributes and behavior from Rectangle"""
        self.assertTrue(hasattr(self.s4, "width"))
        self.assertTrue(hasattr(self.s4, "height"))
        self.assertTrue(hasattr(self.s4, "x"))
        self.assertTrue(hasattr(self.s4, "y"))
        self.assertTrue(hasattr(self.s4, "id"))

        self.s4.width = 10
        self.s4.height = 15
        self.s4.x = 5
        self.s4.y = 7
        self.s4.id = 20

        self.assertTrue(self.s4.width, 10)
        self.assertTrue(self.s4.height, 10)  # Height should == width
        self.assertEqual(self.s4.x, 5)
        self.assertEqual(self.s4.y, 7)
        self.assertEqual(self.s4.id, 20)


    def test_str(self):
        """Test to override __str__"""
        r = Square(10, 2, 1)
        r_dict = r.to_dictionary()
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(r_dict, expected_output)
