"""
A python unittest for the base module
"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    Note:
        base test class
    """
    def test_init_with_id(self):
        """
        Test that the __init__ method sets the id when provided.
        """
        test_id = 42
        obj = Base(id=test_id)
        self.assertEqual(obj.id, test_id)

    def test_init_without_id(self):
        """
        Test that the __init__ method increments
        __nb_objects when id is not provided.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_multiple_id(self):
        """
        test that check for multiple id
        """
        obj = Base()
        obj1 = Base()
        obj2 = Base(8)
        obj3 = Base()

        self.assertEqual(obj.id, 3)
        self.assertEqual(obj1.id,4)
        self.assertEqual(obj2.id, 8)
        self.assertEqual(obj3.id, 5)

if __name__ == '__main__':
    unittest.main()
