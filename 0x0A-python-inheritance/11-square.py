#!/usr/bin/python3

"""
A module demo of a square inheriting a rectangle
"""


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        :param size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.

        :return: A string containing information about the Square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)

# Square = __import__('11-square').Square
#
# s = Square(13)
#
# print(s)
# print(s.area())
