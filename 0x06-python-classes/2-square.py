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

# my_square_1 = Square(3)
# print(type(my_square_1))
# print(my_square_1.__dict__)

# my_square_2 = Square()
# print(type(my_square_2))
# print(my_square_2.__dict__)

# try:
#     print(my_square_1.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square_1.__size)
# except Exception as e:
#     print(e)

# try:
#     my_square_3 = Square("3")
#     print(type(my_square_3))
#     print(my_square_3.__dict__)
# except Exception as e:
#     print(e)

# try:
#     my_square_4 = Square(-89)
#     print(type(my_square_4))
#     print(my_square_4.__dict__)
# except Exception as e:
#     print(e)