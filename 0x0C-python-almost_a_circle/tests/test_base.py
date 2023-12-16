#!/usr/bin/python3

""" The base module"""


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBase(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Set up default definition"""
        Base._Base__nb_objects = 0

    def test_increment(self):
        """Test if id is incremented correctly."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_assignment(self):
        """Test if id is assined correctly"""
        b1 = Base(100)
        b2 = Base(200)

        self.assertTrue(b1.id, 100)
        self.assertTrue(b2.id, 200)

    def test_type(self):
        """Test if id is of type int"""
        b1 = Base()
        self.assertIsInstance(b1.id, int)

    def test_json(self):
        """Test returns the JSON string representation of list_dictionaries"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        exp_outcome = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, exp_outcome)
