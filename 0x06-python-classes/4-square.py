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
            size (int): The size must be greater than 0
        Errors:
            TypeError: raise a type error if size not an integer
            ValueError: raise an error if size is less than error
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """
        Getter property for the size of the square
        Return:
            The value/size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for the size of the square.

        Parameters:
            value (int): The new size of each side of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        area: 
            calculate the area the square
        """
        return self.__size ** 2

# my_square = Square(89)
# print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# my_square.size = 3
# print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# try:
#     my_square.size = "5 feet"
#     print("Area: {} for size: {}".format(my_square.area(), my_square.size))
# except Exception as e:
#     print(e)
