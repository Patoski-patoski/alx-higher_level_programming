import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_increment(self):
        r1 = Rectangle(1, 2, 93)
        r2 = Rectangle(1, 2, 82, 3)
        r3 = Rectangle(2, 5, 3, 0, 12)

        self.assertTrue(r1.id, 1)
        self.assertTrue(r2.id, 2)
        self.assertTrue(r3.id, 12)

    def test_assignment(self):

        r1 = Rectangle(100, 4)
        r2 = Rectangle(200, 21)

        self.assertTrue(r1.id, 100)
        self.assertTrue(r2.id, 200)

    def test_type(self):

        r1 = Rectangle(28, 21, 1, 2, 3)

        self.assertIsInstance(r1.id, int)


if __name__ == '__main__':
    unittest.main()
