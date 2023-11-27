#!/usr/bin/python3

"""
This script defines a Square class.

The Square class represents a square shape and
provides a simple way to create and manipulate square objects.

Attributes:
    __size (int): The size of each side of the square. Default is 0.

Methods:
    __init__(self, size=0): Initializes a new instance of the Square class.
"""


class Square:

    """
    A class to represent a square.

    Attributes:
        __size (int): The size of each side of the square. Default is 0.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of each side of the square. Default is 0.
        """
        self.__size = size

# my_square = Square(3)
# print(type(my_square))
# print(my_square.__dict__)

# try:
#     print(my_square.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square.__size)
# except Exception as e:
#     print(e)
