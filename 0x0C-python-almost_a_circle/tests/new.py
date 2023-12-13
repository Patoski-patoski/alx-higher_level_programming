import unittest
import io
import sys

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test for Rectangle class"""

    def test_attributes(self):
        """Test to check if id is correctly incremented"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 12)
        r5 = Rectangle(1, 2, 3, 4, 12)

        self.assertTrue(r1.width, 1)
        self.assertTrue(r2.height, 2)
        self.assertTrue(r3.x, 3)
        self.assertTrue(r4.y, 4)
        self.assertTrue(r5.id, 12)

    def test_assignment(self):
        """Test to check if id is assigned corectly"""
        r1 = Rectangle(100, 4)
        r2 = Rectangle(200, 21, 2)

        self.assertTrue(r1.id, 100)
        self.assertTrue(r2.x, 2)

    def test_type(self):
        """Test to check if id is type int"""

        r1 = Rectangle(28, 21, 1, 2, 3)

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

    def test_area(self):
        """Test to display Hash(#)"""
        r1 = Rectangle(3, 6, 2, 1, 3)

    def test_display(self):
        """Test to display hash(#)"""
        r1 = Rectangle(3, 2, 1, 4)
        # Capture the output to stdout
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        # Compare the captured output with the expected output
        r1.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n" * 4 + "###\n###\n"
        self.assertEqual(capturedoutput.getvalue(), expected_output)

    def test_str(self):
        """test to override __str__"""
        r = Rectangle(3, 2, 1, 4, 5)
        expected_output = "[Rectangle] (5) 1/4 - 3/2"
        self.assertEqual(str(r), expected_output)


if __name__ == '__main__':
    unittest.main()
