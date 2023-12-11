"""
a python unittest for rectangle module
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Note:
        rectangle class test case
    """
    def test_id_inheritance(self):
        """
        Note:
            test id
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)

    def test_attributes(self):
        """
        Note:
            test class attributes
        """
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_setters(self):
        """
        Note:
            test width and height setters
        """
        r = Rectangle(1, 1)
        r.width = 10
        r.height = 20
        r.x = 30
        r.y = 40
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)

if __name__ == "__main__":
    unittest.main()
