"""
a pythoon unittest for the sqaure module
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Note:
        base test class
    """
    def test_id_inheritance(self):
        """
        Test id inheritance.
        """
        s = Square(1, 2)
        self.assertEqual(s.id, 1)

    def test_attributes(self):
        """
        Note:
            test class attributes
        """
        s1 = Square(10, 20, 30, 40)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 20)
        self.assertEqual(s1.y, 30)
        self.assertEqual(s1.id, 40)

    def test_setters(self):
        """
        Note:
            test size setter
        """
        s2 = Square(1, 1)
        s2.size = 10
        s2.x = 20
        s2.y = 30
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 20)
        self.assertEqual(s2.y, 30)

    def test_getters(self):
        """
        Note:
            test square size getter values
        """
        s3 = Square(12, 0, 0, 1)
        self.assertEqual(s3.size, 12)
        self.assertEqual(s3.y, 0)
        self.assertEqual(s3.x, 0)

if __name__ == "__main__":
    unittest.main()
