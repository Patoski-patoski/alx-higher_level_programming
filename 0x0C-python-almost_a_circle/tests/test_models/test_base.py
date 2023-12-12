import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Rectangle class"""

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
